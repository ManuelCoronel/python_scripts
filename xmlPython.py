import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
web = urllib.request.urlopen(url, context=ctx).read()
#print(web.decode())

stuff = ET.fromstring(web)
lst = stuff.findall('comments/comment')
sum = 0
for i in lst:
    sum = sum + int(i.find('count').text)

print(sum)    
