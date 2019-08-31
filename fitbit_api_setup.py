import fitbit
import gather_keys_oauth2 as Oauth2 
import datetime
from json import dumps, loads

def getFitbitClient():
    CLIENT_ID = '22DRGH'
    CLIENT_SECRET = '5990430b77b9de227dbdf758b075a868'

    try:
        keys = loads(open("keys.json", 'r').read())
    except FileNotFoundError:
        server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
        server.browser_authorize()
        
        keys=dict()
        token = server.fitbit.client.session.token
        keys['access_token'] = str(token['access_token'])
        keys['refresh_token'] = str(token['refresh_token'])

        save_keys_to_file(server.fitbit.client.session.token)

    auth2_client = fitbit.Fitbit(
        CLIENT_ID,
        CLIENT_SECRET,
        refresh_cb=save_keys_to_file,
        oauth2=True,
        access_token=keys['access_token'],
        refresh_token=keys['refresh_token']
    )

    return auth2_client

def save_keys_to_file(keys):
    open("keys.json", 'w').write(dumps(keys))

def getIntradayHeartrate(client, date=None, interval='1min', startTime=None, endTime=None):
    fmt_date = None
    fmt_startTime = None
    fmt_endTime = None
    
    if date == None:
        fmt_date = 'today'
    else:
        fmt_date = str(date.strftime("%Y-%m-%d"))

    if startTime != None:
        fmt_startTime = startTime.strftime("%H:%M")

    if endTime != None:
        fmt_endTime = endTime.strftime("%H:%M")

    return client.intraday_time_series(
        'activities/heart', 
        base_date=fmt_date, 
        detail_level=interval,
        start_time=fmt_startTime,
        end_time=fmt_endTime
    )

def get_total_walking_minutes(client, date=None):
    return client.activities(date=date)

def get_sleep_data(client, date=None):
    pass

def get_total_steps():
    pass

if __name__ == "__main__":
    getFitbitClient()