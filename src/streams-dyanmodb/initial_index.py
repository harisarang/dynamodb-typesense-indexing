import typesense
import boto3
import simplejson as json

def fetch_dyanmodb():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('IPL-Data')
    scan_kwargs = {}
    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None
        yield response
        
def index(client=None):
    if not client:
        client = typesense.Client({
            'nodes': [{
                'host': 'localhost',
                'port': '8108',
                'protocol': 'http',
            }],
            'api_key': '55CL97li9EyOuG54WobxcAjTwHl3rYRRUQcmelXXrr87HmKn',
            'connection_timeout_seconds': 2
        })
    for response in fetch_dyanmodb():
        if not response:
            raise ValueError("Response cannot be empty")
        else:
            for i in response.get('Items', []):
                i['id'] = str(i['id'])
                i['season'] = int(i['season'])
                i['dl'] = int(i['dl'])
                i['winRun'] = int(i['winRun'])
                i['winWicket'] = int(i['winWicket'])
                client.collections['IPL-Data'].documents.create(i)

def main():
    client = typesense.Client({
        'nodes': [{
            'host': 'i3jcr4k0wfbz6qnup-1.a1.typesense.net',
            'port': '443',
            'protocol': 'https',
        }],
        'api_key': 'AaBOdPwIj7doBybWN5rfiXd12baeudWD',
        'connection_timeout_seconds': 2
    })

    schema = {
        'name': 'IPL-Data',
        'fields': [
            {
                'name'  :  'id',
                'type'  :  'string'
            },
            {
                'name'  :  'season',
                'type'  :  'int32',
                'facet' :  True
            },
            {
                'name'  :  'city',
                'type'  :  'string',
                'facet' :  True
            },
            {
                'name'  :  'date',
                'type'  :  'string'
            },
            {
                'name'  :  'team1',
                'type'  :  'string',
                'facet' :  True
            },
            {
                'name'  :  'team2',
                'type'  :  'string',
                'facet' :  True
            },
            {
                'name'  :  'toss',
                'type'  :  'string'
            },
            {
                'name'  :  'decision',
                'type'  :  'string'
            },
            {
                'name'  :  'result',
                'type'  :  'string'
            },
            {
                'name'  :  'dl',
                'type'  :  'int32'
            },
            {
                'name'  :  'winner',
                'type'  :  'string',
                'facet' :  True
            },
            {
                'name'  :  'winRun',
                'type'  :  'int32'
            },
            {
                'name'  :  'winWicket',
                'type'  :  'int32'
            },
            {
                'name'  :  'mom',
                'type'  :  'string'
            },
            {
                'name'  :  'venue',
                'type'  :  'string',
            },
            {
                'name'  :  'umpire1',
                'type'  :  'string'
            },
            {
                'name'  :  'umpire2',
                'type'  :  'string'
            },
        ],
        'default_sorting_field': 'season'
    }
    client.collections.create(schema)   
    index(client)

if __name__ == '__main__':
    main()