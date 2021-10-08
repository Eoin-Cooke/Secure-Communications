string1 = "label"

string2 = " "

for i in string1:
    string2 += chr(ord(i) ^ 13)

print("crypto{{{}}}".format(string2))