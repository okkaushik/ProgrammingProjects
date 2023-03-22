import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input("Enter Count: "))
position = int(input("Enter Position: "))
countcompleted = int(0)
currentposition = int(1)
while countcompleted <= count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        if currentposition == position:
            print("Retrieving:", url)
            url = (tag.get('href', None))
            currentposition = int(1)
            countcompleted = countcompleted + int(1)
            break
        else:
            currentposition = currentposition + int(1)
