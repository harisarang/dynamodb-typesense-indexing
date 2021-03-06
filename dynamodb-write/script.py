import boto3
import csv

def main():
    dyanmodb = boto3.client('dynamodb')
    count = 0;
    with open('IPL Data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            matchid = row['id']
            season = row['season']
            city = row['city']
            date = str(row['date'])
            team1 = row['team1']
            team2 = row['team2']
            toss = row['toss_winner']
            decision = row['toss_decision']
            result = row['result']
            dl =  row['dl_applied']
            winner = row['winner']
            winRun = row['win_by_runs']
            winWicket = row['win_by_wickets']
            mom = row['player_of_match']
            venue = row['venue']
            umpire1 = row['umpire1']
            umpire2 = row['umpire2']
            # print(f'{matchid}, {season}, {city} {date}, {team1}, {team2}, {toss}, {decision}, {result}, {dl}, {winner}, {winRun}, {winWicket}, {mom}, {venue}, {umpire1}, {umpire2}')
            try:
                response = dyanmodb.put_item(
                TableName='IPL-Data',
                Item={
                        'id' : {'N':str(matchid)},
                        'season': {'S': season},
                        'city': {'S':city},
                        'date': {'S': str(date)},
                        'team1': {'S': team1},
                        'team2': {'S': team2},
                        'toss': {'S': toss},
                        'decision': {'S': decision},
                        'result': {'S': result},
                        'dl': {'N': str(dl)},
                        'winner': {'S': winner},
                        'winRun': {'N': str(winRun)},
                        'winWicket': {'N': str(winWicket)},
                        'mom': {'S': mom},
                        'venue': {'S': venue},
                        'umpire1': {'S': umpire1},
                        'umpire2': {'S': umpire2},
                    }
                )
                count = count + 1
            except Exception as e:
                print(e)
    print(count)

if __name__ == '__main__':
    main()