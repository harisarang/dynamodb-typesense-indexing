import boto3
import json

def test_status():
    dyanmodb = boto3.client('dynamodb')
    response = dyanmodb.describe_table(
        TableName='IPL-Data'
    )
    # response = json.load(response)
    print(response['Table'])

if __name__ == '__main__':
    test_status()