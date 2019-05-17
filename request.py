import requests
from xml.etree import ElementTree as ET
import urllib.request

apiid = "&appid="
url = "https://api.openweathermap.org/data/2.5/forecast?id=756135&mode=xml"

def url_builder(city_id):
    user_api = 'c02220684b687f7251cf2f50a6495450'  # Obtain yours form: http://openweathermap.org/
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/forecast?id='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

    full_api_url = api + str(city_id) + '&mode=xml&units=' + unit + '&APPID=' + user_api
    print(full_api_url)
    return full_api_url


def data_fetch(full_api_url):
    url = requests.get(full_api_url)
    tree = ET.fromstring(url.text)
    # output = url.read().decode('utf-8')
    # raw_api_dict = json.loads(output)
    # url.close()
    # return raw_api_dict
    # root = tree.getroot()
    r2= ET.ElementTree(tree)
    r2.write("data/file10.xml")
    print(tree)


def main():
    cityID= "756135"
    data_fetch(url_builder(cityID))

main()