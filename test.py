import requests


request_bbc_status_code = requests.get('https://www.bbc.co.uk/iplayer/live/bbcnews')
"""print(request_bbc_status_code.status_code)
print(request_bbc_status_code.headers)
print(request_bbc_status_code.content)"""
if request_bbc_status_code.status_code == 200:
    print('SUCCESS')
else:
    print("BAD")
