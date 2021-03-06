import boto3

def main():
    dyanmodb = boto3.client('dynamodb')
    try:
        response = dyanmodb.put_item(
        TableName='IPL-Data',
        Item={
                'id' : {'N': str(50000)},
                'season': {'S': '2020'},
                'city': {'S':'Chennai'},
                'date': {'S': '12/31/17'},
                'team1': {'S': 'Kolkata Knight Riders'},
                'team2': {'S': 'Mumbai Indians'},
                'toss': {'S': 'Mumbai Indians'},
                'decision': {'S': 'field'},
                'result': {'S': 'normal'},
                'dl': {'N': str(0)},
                'winner': {'S': 'Mumbai Indians'},
                'winRun': {'N': str(0)},
                'winWicket': {'N': str(4)},
                'mom': {'S': 'N Rana'},
                'venue': {'S': 'Wankhede Stadium'},
                'umpire1': {'S': 'CK Nandan'},
                'umpire2': {'S': 'Nitin Menon'},
            }
        )
        print('Success')
    except Exception as e:
        print(e)

def delete():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('IPL-Data')
    try:
        response = table.delete_item(
            Key={
                'id': 50000
            }
        )
        print('Success')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main() if 1 else delete()