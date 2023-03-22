fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print("Invalid file, please try again")
    quit()
count = 0
for line in fh:
    line = line.split()
    if "From:" in line:
        continue
    elif "From" in line:
        address = line[1]
        print(address)
        count = count + 1
    else:
        continue
print("There were", count, "lines in the file with From as the first word")
