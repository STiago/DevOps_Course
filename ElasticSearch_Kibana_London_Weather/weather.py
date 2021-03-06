#!/opt/Python-2.7/bin/python

import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError

ROOT_URL = "http://www.bbc.co.uk/weather/"

def get_weather_info(start_date, end_date):
    weather_dic = {}
    soup = BeautifulSoup(urllib2.urlopen(ROOT_URL + "2643743"), "html.parser")
    table = soup.find('div', {'class': 'daily-window'})

    sday = table.find('span', {'class': 'day-name'})
    day = sday['aria-label'] #Current day 
    
    sweather = table.find('span', {'class': 'weather-type-image weather-type-image-40'})
    weather = sweather['title'] #Weather
    
    list_temp = []
    stemp = table.find('span', {'class': 'units-value temperature-value temperature-value-unit-c'})
    for item in stemp:
        list_temp.append(item)
    temperature = int(list_temp[0]) #Temperature

    swind = table.find('span', {'class': 'wind wind-speed windrose-icon windrose-icon--average windrose-icon-40 windrose-icon-40--average wind-direction-sw'})
    wind = swind['data-tooltip-kph'] #WindDirection
    aux_wind = wind.split(" ")
    windspeed = int(aux_wind[0])
    winddirection = aux_wind[2] + aux_wind[3]

    weather_dic = {'day': day, 'weather': weather, 'temperature':temperature, 'windspeed': windspeed, 'winddirection': winddirection}
    return weather_dic     


def send_file_elastic_search(index, doc, contain, host):
    end = False
    elastic_search = Elasticsearch(host)
    while not end:
        try:
            elastic_search.index(index, doc, contain)
            end = True
            print "Sending: ", contain
        except ConnectionError:
            pass


def report_weather(start_date, end_date):
    host = [{"host": "localhost", "port": 9200}]
    weather_dict = get_weather_info(start_date, end_date)
    send_file_elastic_search('weather', 'weather', weather_dict, host)
    


def main(start_date=None, end_date=None):
    now = datetime.utcnow()
    if not start_date:
        start_date = datetime(year=now.year,
                              month=now.month,
                              day=now.day,
                              hour=now.hour)
    if not end_date:
        end_date = datetime(year=now.year,
                              month=now.month,
                              day=now.day)
    print "\nDay: " + str(start_date) + ", to: " + str(end_date)
    report_weather(start_date, end_date)


if __name__ == "__main__":
    main()
