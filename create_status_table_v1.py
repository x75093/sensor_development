from __future__ import print_function 
import boto3
import sys

dynamodb = boto3.resource('dynamodb')
status_table_name = sys.argv[1]

table = dynamodb.create_table(
    TableName = str(status_table_name),
    KeySchema = [
        {
            'AttributeName': 'Location',
            'KeyType': 'HASH'  #Partition key
        },
    ],
    AttributeDefinitions=[
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