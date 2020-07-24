import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(data)
print('User count:', len(info))
items = info["comments"]
sum = 0
for item in items:
    sum = sum + item["count"]
    print(item["count"])
print("the sum is ",sum)
