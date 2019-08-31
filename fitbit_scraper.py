import fitbit_api_setup as fas
from pprint import pprint as pp
import datetime as dt
import sys, getopt
import helpers

interval = '1min'
specifiedDate = dt.datetime.today()

valid_intervals = [
    '1min',
    '15min'
]

def usage():
    print("Usage: python fitbit_scraper.py [-d DATE] [-i {1min|15min}]")
    print("DATE must be in format YYYY-MM-DD")

try:
    opts, args = getopt.getopt(sys.argv[1:], "hd:i:")
except getopt.GetoptError as err:
    # print help information and exit:
    print(err) # will print something like "option -a not recognized"
    usage()
    sys.exit(2)
    
for o, a in opts:
    if o == "-d":
        try:
            specifiedDate = dt.datetime.strptime(a, "%Y-%m-%d")
        except ValueError:
            print("Date (-d) must be in format YYYY-MM-DD")
            sys.exit(2)
    elif o == "-i":
        if a in valid_intervals:
            interval=a
        else:
            print("Interval option (-i) must be one of the following: ", valid_intervals)
            sys.exit(2)
    elif o == '-h':
        usage()
        sys.exit()
    else:
        assert False, "unhandled option"

client = fas.getFitbitClient()
data = fas.getIntradayHeartrate(
    client,
    date=specifiedDate,
    interval=interval,
)
hrdata = data['activities-heart-intraday']['dataset']
helpers.saveDataToCSV(hrdata, "output/" + specifiedDate.strftime('%Y_%m_%d') + " - heartrate.csv")


