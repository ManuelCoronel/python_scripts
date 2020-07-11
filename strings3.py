text = 'X-DSPAM-Confidence:    0.8475'

pos = text.find(' ')
#print((text[19:]).lstrip)
str2 = text[pos:]
str2 = str2.lstrip()
print(float(str2))
#print(str2).
# print(float(str2))
