from __future__ import division
import time
import boto3
import json
from decimal import Decimal
import pyupm_th02 as upmth02
from datetime import datetime
from StringIO import StringIO
import sys
import subprocess

## Read command line input arguments
if len(sys.argv) == 4:
    temp_table_name = str(sys.argv[1])
    status_table_name = str(sys.argv[2])
    this_node = str(sys.argv[3])

elif len(sys.argv) > 4:
    temp_table_name = str(sys.argv[1])
    status_table_name = str(sys.argv[2])
    this_node = str(sys.argv[3])
    #read_limit = int(sys.argv[4])
    temp_loop_limit = int(sys.argv[4])
    temp_loop_sleep = int(sys.argv[5])
else:
    print("run_temp_v2.py requires 3 or 5 arguments via the command line")
    print("only", len(sys.argv), "argument passed") 
    print("1: Temperature Table Name")
    print("2: Status Table Name")
    print("3: Device Name")
    # print("4: Read Limit")
    print("4: Average Reading Amount (int) ex. 10")
    print("5: Time between reads (int) ex. 60")
    sys.exit(0)

## Initatiate Tables from AWS
dynamodb = boto3.resource('dynamodb')
table_temp = dynamodb.Table(temp_table_name)
table_status = dynamodb.Table(status_table_name)

## Initate status read from AWS                                                 
status_response = table_status.get_item( Key = { 'Location' : this_node } )     
item = status_response[ 'Item' ]                                                
this_status = item[ 'Status' ]

## Update Status Table
ip_address = subprocess.Popen("ip route get 1 | awk '{print $NF;exit}'", stdout=subprocess.PIPE, shell=True).communicate()[0]
date = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True).communicate()[0]
user = subprocess.Popen("who", stdout=subprocess.PIPE, shell=True).communicate()[0]
table_status.put_item(Item={'Location': this_node, 'Status': this_status, 'IP Address': ip_address, 'User Logs': user, 'DTG': date,})

## Take temperature readings
reading_number = 0

## Initiate Temperature Sensor
th02_sensor = upmth02.TH02()

while this_status == 1:
    
    ## possibly execute systems check and update status with 
    ## table.put_item(Item={'Location': this_node,'Status': this_status,})
    
    ## read status from AWS
    status_response = table_status.get_item( Key = { 'Location' : this_node } )
    item = status_response[ 'Item' ]
    this_status = item[ 'Status' ]
    
    ## Update iteration
    reading_number += 1
    
    ## Grove Reading of temperature and humidity
    humid = 0
    temp = 0 
    for i in xrange(temp_loop_limit):
        humid += Decimal( th02_sensor.getHumidity())
        temp += Decimal( th02_sensor.getTemperature() * 9.0/5.0 + 32.0)
        
        ## Delay for different time spread readings 
        time.sleep( temp_loop_sleep )    
    avg_humid = Decimal( humid / temp_loop_limit )
    avg_temp = Decimal( temp / temp_loop_limit )

    ## Update DTG
    date = datetime.strftime( datetime.now() , '%Y-%m-%d %H:%M:%S' )
    
    ##Write info
    table_temp.put_item( Item = {'DTG': date, 'Location': this_node, 'Temperature': avg_temp, 'Humidity': avg_humid, 'Status': this_status,
                                'Read_Number': reading_number, } )
    
    # NOTE: This feature not used in run_temp3.py3
    ## Limit total number of reads
    #if reading_number == read_limit:
    #    this_status = 0
