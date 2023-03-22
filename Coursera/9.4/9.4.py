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
        email = words[1]
        counts[email] = counts.get(email,0) + 1

largemail = None
largecount = None
for key,value in counts.items():
    if largecount is None or value > largecount:
        largemail = key
        largecount = value

print(largemail,largecount)
