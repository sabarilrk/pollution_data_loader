import requests
import json
from Model.pollution_model import PollutionModel

def get_pollution_date(url):
    res_list=[]
    _url=url
    data = requests.get(url)
    data_dict = data.json()

    print(data_dict['records'])
    for i in data_dict['records']:
        trans_rec = transform(i)
        res_list.append(list(trans_rec.dict().values()))
    print(res_list)
def transform(row:dict)->PollutionModel:
    obj = PollutionModel(**row)
    return obj

if __name__ == '__main__':
    api_key = "579b464db66ec23bdd000001733643dae604467b4345307681dd876c"
    url = "https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key={api_key}&format=json&offset=0&limit=2000".format(api_key=api_key)

    get_pollution_date(url)