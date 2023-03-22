import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input("Enter Count: "))
position = int(input("Enter Position: "))
times_attempted = 0
repititions = 0
currentlink = None
tags = soup('a')

while times_attempted < count:
    for tag in tags:
        repititions = int(repititions) + 1
        if repititions == position:
            currentlink = (tag.get('href', None))
            print("Retrieving:", currentlink)
            repititions = 0
            times_attempted = times_attempted + 1
            break
#THIS CODE IS BROKEN
#THIS CODE IS BROKEN
#THIS CODE IS BROKEN
#THIS CODE IS BROKEN
#THIS CODE IS BROKEN
