import typesense
import simplejson as json

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
    search_parameters = {
        'q'         : '50000',
        'query_by'  : 'id',
    }
    response = client.collections['IPL-Data'].documents.search(search_parameters)
    print(json.dumps(response, indent=4))

if __name__ == '__main__':
    main()