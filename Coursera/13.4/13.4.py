import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
try:
    xml = urllib.request.urlopen(url, context=ctx).read()
    print("Retrieving:",url)
except:
    print("Invalid URL")
    quit()

tree = ET.fromstring(xml)
lst = tree.findall('comment')
counts = len(lst)
totalsum = 0

for item in lst:
    totalsum = totalsum + item.find('count').text

print(counts)
print(totalsum)
