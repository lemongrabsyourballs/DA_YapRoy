import requests
URL = "http://172.17.50.43/varsity"
r = requests.get(URL)
print(r.text)
print("Status code:")
print("\t*", r.status_code)
h = requests.head(URL)
print("Header:")
print("**********")
for x in h.headers:
    print("\t" ,x,":",h.headers[x])
print("*********")