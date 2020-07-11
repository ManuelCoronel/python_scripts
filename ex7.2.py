name = input("Enter the name from the file")
text = open(name)
total = 0
con = 0
for lines in text:

    if "X-DSPAM-Confidence:" in lines:
        h = lines
        print(h)
        pos = lines.find(":")
        pos = pos + 1
        str4 = lines[pos:]
        str4 = str4.strip()
        total = total+float(str4)
        con = con + 1
        print(total)

print(total/con)
