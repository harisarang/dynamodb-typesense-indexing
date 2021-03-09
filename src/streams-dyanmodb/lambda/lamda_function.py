import json
import typesense

def lambda_handler(event, context):
    client = typesense.Client({
        'nodes': [{
            'host': 'i3jcr4k0wfbz6qnup-1.a1.typesense.net',
            'port': '443',
            'protocol': 'https',
        }],
        'api_key': 'AaBOdPwIj7doBybWN5rfiXd12baeudWD',
        'connection_timeout_seconds': 2
    })
    processed = 0
    atrributes = {
        'id' : 'N',
        'season': 'S',
        'city': 'S',
        'date': 'S',
        'team1': 'S',
        'team2': 'S',
        'toss': 'S',
        'decision': 'S',
        'result': 'S',
        'dl': 'N',
        'winner': 'S',
        'winRun': 'N',
        'winWicket': 'N',
        'mom': 'S',
        'venue': 'S',
        'umpire1': 'S',
        'umpire2': 'S',
    }
    for record in event['Records']:
        ddb_record = record['dynamodb']
        if record['eventName'] == 'REMOVE':
            res = client.collections['IPL-Data'].documents[str(ddb_record['OldImage']['id']['N'])].delete()
        else:
            upload = ddb_record['NewImage']
            record1 = {}
            for key in atrributes.keys():
                record1[key] = upload['NewImage'][key][atrributes[key]]
            record1['id'] = str(record1['id'])
            record1['season'] = int(record1['season'])
            record1['dl'] = int(record1['dl'])
            record1['winRun'] = int(record1['winRun'])
            record1['winWicket'] = int(record1['winWicket'])
            res = client.collections['IPL-Data'].upsert(record1)
            print(res)
        processed = processed + 1

    print('Successfully processed {} records'.format(processed))
    return processed
