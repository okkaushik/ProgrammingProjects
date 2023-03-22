# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file name")
    quit()
x = 0
totalvalue = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        decvalue = line.strip()
        colonnum = decvalue.find(":")
        colonnum = int(colonnum) + 1
        decvalue = decvalue[colonnum:]
        x = x + 1
        count = float(x)
        totalvalue = float(totalvalue) + float(decvalue)
averagevalue = totalvalue / count
print("Average spam confidence:", averagevalue)
