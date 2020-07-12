import re



#tex = input("Enter file \n")
text = open("RegularExpression2.txt")
data = list()
sum = 0
for line in text :
    x = re.findall('([0-9]+)',line)

    if len(x) > 0 :
        data.append(x)
        for y in x :
            sum = sum + int(y)

print(sum)
