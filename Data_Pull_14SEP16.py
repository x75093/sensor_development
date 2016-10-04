import time
import boto3
import json
from decimal import Decimal
from datetime import datetime
from StringIO import StringIO
import sys
import numpy as np
import csv

if len(sys.argv) == 6:
    temp_table_name = str(sys.argv[1])
    output_table_name = str(sys.argv[2])
    region_name = str(sys.argv[3])
    aws_access_key_id = str(sys.argv[4])
    aws_secret_access_key = str(sys.argv[5])
    
elif len(sys.argv) == 3:
    temp_table_name = str(sys.argv[1])
    output_table_name = str(sys.argv[2])
    region_name='us-east-1'
    aws_access_key_id='junk1'
    aws_secret_access_key='junk2'


else:
    temp_table_name = str(sys.argv[1])
    output_table_name = str(sys.argv[2])
    region_name='us-east-1'
    aws_access_key_id='junk1'
    aws_secret_access_key='junk2'




dynamodb = boto3.resource('dynamodb', region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key)


##### Read In ######

## Ref from: http://stackoverflow.com/questions/36780856/complete-scan-of-dynamodb-with-boto3 ##


table = dynamodb.Table(temp_table_name)

response = table.scan()
data = response['Items']

while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items'])


##### Write out ######
## Ref From: http://stackoverflow.com/questions/10373247/how-do-i-write-a-python-dictionary-to-a-csv-file ##


with open(output_table_name , 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, data[0].keys())
    w.writeheader()
    for i in range(len(data)):
        w.writerow(data[i])




