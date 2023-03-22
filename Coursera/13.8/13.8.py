import json
import urllib.request, urllib.parse, urllib.error

url = input("Enter location: ")

print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

js = json.loads(data)
totalsum = 0
count = 0

for item in js["comments"]:
    value = item["count"]
    intvalue = int(value)
    totalsum = totalsum + intvalue
    count = count + 1

print("Count:", count)
print("Sum", totalsum)
