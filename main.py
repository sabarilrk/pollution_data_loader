import requests
import json

def get_pollution_date(url):
    _url=url
    data = requests.get(url)
    data_dict = data.json()

    print(data_dict['records'])

if __name__ == '__main__':
    api_key = "579b464db66ec23bdd000001733643dae604467b4345307681dd876c"
    url = "https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key={api_key}&format=json".format(api_key=api_key)

    get_pollution_date(url)