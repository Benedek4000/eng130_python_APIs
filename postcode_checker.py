import test as ts
import requests

url = "http://api.postcodes.io/postcodes/"

postcode = "m345ly"

url_arg = url + postcode

response = requests.get(url_arg)

response_dict = response.json()['result']

#[print(key, value) for key, value in response_dict.items()]
print(ts.get_value(response_dict, 'european_electoral_region'))
print(ts.check_postcode(url, postcode))
print(f"{url}\n{postcode}")
print(type(response))
[print(key, value) for key, value in response_dict.items()]
