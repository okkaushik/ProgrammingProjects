fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("invalid file, please try again")
    quit()
lst = list()
newlst = list()
for line in fh:
    testlst = line.split()
    lst = lst + testlst
for word in lst:
    if word not in newlst:
        newlst.append(word)
newlst.sort()
print(newlst)
