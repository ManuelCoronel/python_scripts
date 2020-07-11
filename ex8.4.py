fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for i in fh:
    str = i.split()
    print(str)
    for j in str:

        if not j in lst:
            print(j)
            lst.append(j)

lst.sort()
print(lst)
