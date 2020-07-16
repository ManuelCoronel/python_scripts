# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
rep =int(input())
pos =int(input())
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
index = 1
cadena = "Fikret"
tags = soup('a')
while rep > 0 :
    for tag in tags:
        if pos == index :
            cadena = cadena+" " + tag.contents[0]
            url = tag.get('href',None)
    #    print('TAG:', tag)
    #    print('URL:', tag.get('href', None))
    #    print('Contents:', tag.contents[0])
    #    print('Attrs:', tag.attrs)
        index = index + 1

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    index = 1
    rep = rep - 1


print(cadena)
