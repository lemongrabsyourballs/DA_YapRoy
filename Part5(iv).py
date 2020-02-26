import requests
URL = "http://172.17.50.43/varsity"
r = requests.get(URL)
headers = {
    'User-Agent':'Mobile'
}
URL2 = 'http://httpbin.org/headers'
rh = requests.get(URL2, headers=headers)
print(rh.text)