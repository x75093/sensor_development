from __future__ import print_function 
import boto3
import sys
from decimal import Decimal

if len(sys.argv) == 4:
	status_table_name = str(sys.argv[1])
	this_node = str(sys.argv[2])
	this_status = Decimal(sys.argv[3])
elif len(sys.argv) > 4:
	status_table_name = str(sys.argv[1])
	this_node = str(sys.argv[2])
	this_status = Decimal(sys.argv[3])
	ip_address = str(sys.argv[4])
	user = str(sys.argv[5])
	date = str(sys.argv[6])
else:
	print("update_status_table_v2.py requires 3 or 6 arguments via the command line")
        print("only", len(sys.argv), "argument passed") 
	print("1: Status Table Name")
        print("2: Device Name")
        print("3: Status (1 or 0)")
        print("4: IP Address")
        print("5: Username")
        print("6: Date", "\n")
	sys.exit(0)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(str(status_table_name))

table.put_item(Item={'Location': this_node,'Status': this_status, 'IP Address': ip_address, 'User Logs': user, 'DTG': date,})

print("Table status:", table.table_status)
