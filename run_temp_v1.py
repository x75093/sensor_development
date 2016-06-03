import time
import boto3
import json
from decimal import Decimal
import pyupm_grove as grove
from datetime import datetime
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
import sys
#import numpy as np

## Read command line input arguments
temp_table_name = str(sys.argv[1])
status_table_name = str(sys.argv[2])
this_node = str(sys.argv[3])
read_limit = int(sys.argv[4])



## Initatiate Tables from AWS
dynamodb = boto3.resource('dynamodb')
table_temp = dynamodb.Table(temp_table_name)
table_status = dynamodb.Table(status_table_name)

## Create the temperature sensor object using AIO pin 0


## Initate status read from AWS
status_response = table_status.get_item( Key = { 'Location' : this_node } )
item = status_response[ 'Item' ]
this_status = item[ 'Status' ]


## Take 10 temperature readings
reading_number = 0


while this_status == 1:
    
    ## possibly execute systems check and update status with 
    ## table.put_item(Item={'Location': this_node,'Status': this_status,})
    
    
    ## read status from AWS
    status_response = table_status.get_item( Key = { 'Location' : this_node } )
    item = status_response[ 'Item' ]
    this_status = item[ 'Status' ]
    
    ## Update iteration
    reading_number += 1
    
    ## Replace with Grove Reading
    temp = grove.GroveTemp(0)
    celsius = temp.value() 
    
    ## Delay for different time spread readings
    time.sleep( 10 )
    
    ## Update DTG
    date = datetime.strftime( datetime.now() , '%Y-%m-%d %H:%M:%S' )
    
    ##Write info
    table_temp.put_item( Item = {'DTG': date, 'Location': this_node, 'Temperature': celsius, 'Status': this_status,
                                'Read_Number': reading_number, } )
    
    ## Limit total number of reads
    if reading_number == read_limit:
        this_status = 0




