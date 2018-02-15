import requests
import csv
from io import open as iopen

def reading_satellite(csvforimport,APIkey,zoom,size):
    API_KEY = APIkey
    base = "https://maps.googleapis.com/maps/api/staticmap?scale=2&size="
    locations = []
    with open(csvforimport, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            ind, lat, lng = int(row[0]),float(row[1]),float(row[2])


            location = (ind, lat, lng)
            locations.append(location)
    for location in locations:
        ind, lat, lng = location
        latlng = "center={},{}".format(lat, lng)
        view = "zoom={}&maptype=satellite".format(zoom)
        keys = "key={}".format(API_KEY)
        url = "{}{}x{}&{}&{}&{}".format(base,size,size, latlng, view, keys)
        filename = "{}_{}_{}_{}.png".format(ind,lat,lng,zoom)
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            with iopen(filename, 'wb') as file:
                file.write(res.content)
            print(filename)
        else:
            return False

reading_satellite("./lights_no_people_DRC_clean.csv","AIzaSyCEz-78bIwW_uko7VOmde8YoWBhiXg6e0E",13,640)
