from __future__ import print_function 
import boto3
import sys
from decimal import Decimal

status_table_name = sys.argv[1]
this_node = str(sys.argv[2])
this_status = Decimal(sys.argv[3])

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(str(status_table_name))

table.put_item(Item={'Location': this_node,'Status': this_status,})

print("Table status:", table.table_status)
