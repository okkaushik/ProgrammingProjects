from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
count = 0
totalnum = 0
for tag in tags:
    number = int(tag.contents[0])
    totalnum = totalnum + number
    count = count + 1

print("Count", count)
print("Sum", totalnum)
