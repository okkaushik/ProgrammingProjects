import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter location: ")
print("Retrieving", url)
document = urllib.request.urlopen(url,).read()
print("Retrieved", len(document),"characters")

tree = ET.fromstring(document)
counts = tree.findall('.//count')
totalsum = 0
for item in counts:
    value = item.text
    totalsum = totalsum + int(value)

print("Counts:",len(counts))
print("Sum",totalsum)
