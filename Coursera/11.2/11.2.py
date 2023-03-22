name = input("Enter file:")
try:
    handle = open(name)
except:
    print("Invalid file")
    quit()

import re

totalvalue = 0

for line in handle:
    x = re.findall('[0-9]+', line)
    for item in x:
        intnum = int(item)
        totalvalue = totalvalue + intnum

print(totalvalue)
