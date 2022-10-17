import requests


def get_value(resp_dict, value):
    return resp_dict[value]


def check_postcode(url, postcode):
    response = requests.get(url+postcode.replace(' ','').lower())
    if response.status_code == 200:
        if response.json()['result']['postcode'].replace(' ','').lower() == postcode.replace(' ','').lower():
            return('Valid Postcode')
        else:
            return('Invlaid Postcode')
    else:
        return f"STATUS CODE {response.status_code}"



url = "http://api.postcodes.io/postcodes/"

postcode = "m345ly"

url_arg = url + postcode

response = requests.get(url_arg)

response_dict = response.json()['result']

#[print(key, value) for key, value in response_dict.items()]
print(f"Postcode: {response_dict['postcode']}")
print(f"Longitude: {response_dict['longitude']}   latitude: {response_dict['latitude']}")

