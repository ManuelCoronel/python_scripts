# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = dict()
for line in handle:
    if line.startswith('From '):
        str = line.split()
        #print(str[5])
        str2 = str[5].split(':')
        #print(str2)
        hours[(str2[0])]=hours.get((str2[0]),0)+1

#sprint(hours)
ordenados = list()
tem = list()
ordenados = hours.items()



ordenados = sorted(ordenados)
for i,j in ordenados:
    print(i,j)
