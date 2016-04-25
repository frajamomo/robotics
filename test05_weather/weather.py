#!/usr/bin/env python
import requests
import sys
sys.path.append("../test04_lcd/")

import lcddriver
from time import sleep
from datetime import datetime


#lcd = lcddriver.lcd()

# Yahoo Weather City ID's more available at https://weather.yahoo.com
cities = [ ('Amsterdam', '727232'),
           ('Madrid', '766273'),
           ('Bangkok',  '1225448'),
           ('Beijing', '2151330'),
           ('Berlin', '638242'),
           ('Chicago', '2379574'),
           ('Istanbul', '2344116'),
           ('London',   '44418'),
           ('Los Angeles', '12795609'),
           ('Montreal', '3534'),
           ('Mumbai', '2295411'),
           ('New York', '2459115'),
           ('Paris', '615702'),
           ('Stockholm', '906057'),
           ('Tokyo', '1118370'),
           ('Venice', '725746'),
           ('Warsaw', '523920') ]

city_codes = ",".join([c[1] for c in cities])

def getWeatherConditions() :
    try :
        url = 'https://query.yahooapis.com/v1/public/yql'
        # encode query string for request
        query = ("select item.condition from weather.forecast where woeid in ("
                        + city_codes + ") and u='c'")
        query_strings = {'q': query, 'format' : 'json'}
        # headers to disable caching (in theory)
        headers = {'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}
        # get weather data from Yahoo
        r = requests.get(url, params=query_strings, headers=headers)
        # return data formatted to JSON
        return r.json()
    except Exception:
        return "Feed Error"

if __name__ == "__main__":
    lcd = lcddriver.lcd()
    while 1:
        data = getWeatherConditions()
        if( type(data) != type(dict()) or "error" in data):
            # Error
            print (data)
            #lcd.lcd_clear()
            #lcd.lcd_display_string("FEED ERROR", 1)
            sleep(4)
        else:
            count = data["query"]["count"]
            # Loop through cities
            for c in range(0, count):
                # Retrieve city name, condition and temperature
                city = cities[c][0]
                cond = data["query"]["results"]["channel"][c]["item"]["condition"]["text"]
                temp = data["query"]["results"]["channel"][c]["item"]["condition"]["temp"]
                lcd.lcd_clear()
                lcd.lcd_display_string('{:^16}'.format(city), 1)
                lcd.lcd_display_string("%-13.13s %2s" % (cond, temp), 2)
                # Display city temperature and condition
                print "%-14.14s %2s" % (cond, temp)
                sleep(3)


