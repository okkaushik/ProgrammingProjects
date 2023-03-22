name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print("Invalid file")
    quit()

counts = dict()

for line in handle:
    if "From:" in line:
        continue
    elif "From" in line:
        words = line.split()
        hour = words[5]
        hour = hour.split(":")
        hour = hour[0]
        counts[hour] = counts.get(hour,0) + 1

lst = counts.items()
lst = sorted(lst)

for hour,freq in lst:
    print(hour,freq)
