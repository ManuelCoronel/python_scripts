name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

text = open(name)
lst =list()
mymap = dict()

for line in text:
    if line.startswith('From '):
        str = line.split()
        mymap[str[1]] = mymap.get(str[1],0)+1

maxKey = None
maxValue = None
for key,value in mymap.items():
    if (maxKey is None and maxValue is None) or (maxValue <= value):
        maxKey = key
        maxValue = value


print(maxKey,maxValue)
