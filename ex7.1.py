name = input("Enter the name form the file")
text = open(name)

for line in text:
    str3 = line.rstrip()
    str3 = str3.upper()
    print(str3)
    
