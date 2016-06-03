from __future__ import print_function # Python 2/3 compatibility
import boto3
import sys

dynamodb = boto3.resource('dynamodb')
temp_table_name = sys.argv[1]

table = dynamodb.create_table(
    TableName = str(temp_table_name),
    KeySchema=[
        {
            'AttributeName': 'DTG',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'Location',
            'KeyType': 'RANGE'  #Sort key
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'DTG',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Location',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table status:", table.table_status)