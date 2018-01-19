import math
import csv
import webbrowser
import urllib
import io
import requests


def distance_between(lat_1, lon_1, lat_2, lon_2):
    '''Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them'''
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1) * math.sin(lat_2) + math.cos(lat_1) * math.cos(lat_2) * math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06  # 69.09 = circumference of earth in miles / 360 degrees

    return dist


def get_address(data):
    address = ''
    for i in range(3):
        address += closest_wendys[i + 4]
        address = address.replace(' ', '+')
    web_address = 'http://maps.google.com/maps?q=' + address

    return web_address


csv_url = 'http://cs1110.cs.virginia.edu/files/wendys.csv'

case = 0
while case not in [1, 2, 3]:
    case = int(input('urllib, requests, local file: 1/2/3 '))
    if case == 1:
        print('Using urllib \n')
        raw_csv = urllib.request.urlopen(csv_url)
        wendys_data = list(csv.reader(io.TextIOWrapper(raw_csv)))  # https://stackoverflow.com/a/21351911
        break

    elif case == 2:
        print('Using requests \n')
        raw_csv = requests.get(csv_url).text
        data_text = raw_csv.splitlines()
        wendys_data = []
        for items in data_text: wendys_data.append(items.split(','))
        break

    elif case == 3:
        print('Using local file \n')
        raw_csv = open('wendys.csv')
        wendys_data = list(csv.reader(raw_csv))
        break

user_location = input('What is your latitude and longitude? latitude, longitude: ').split(',')
user_lat = float(user_location[0])
user_lon = float(user_location[1])

closest_location = 7917.5  # Diameter of the Earth

for counter, store_info in enumerate(wendys_data):
    wendys_lat = float(store_info[0])
    wendys_lon = float(store_info[1])
    locations_distance = distance_between(user_lat, user_lon, wendys_lat, wendys_lon)
    if locations_distance < closest_location:
        closest_location = locations_distance
        which_store = counter

closest_wendys = wendys_data[which_store]

webbrowser.open(get_address(closest_wendys))
