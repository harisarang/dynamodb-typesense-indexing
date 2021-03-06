import typesense

def main():
    client = typesense.Client({
            'nodes': [{
                'host': 'localhost',
                'port': '8108',
                'protocol': 'http',
            }],
            'api_key': '55CL97li9EyOuG54WobxcAjTwHl3rYRRUQcmelXXrr87HmKn',
            'connection_timeout_seconds': 2
        })
    search_parameters = {
        'q'         : 'Royal Challengers Bangalore',
        'query_by'  : 'team1',
    }
    response = client.collections['IPL-Data'].documents.search(search_parameters)
    print(response)

if __name__ == '__main__':
    main()