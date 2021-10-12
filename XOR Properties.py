from binascii import unhexlify

def xor(x1, x2):
    
    code1 = " "
    code2 = " "
    
    if len(code1) != len(code2):
        print("Error")
    
    return " ".join(format(int(a1, 16) ^ int(a2, 16), "b") for a1, a2 in zip(x1, x2))

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"

key2 = xor("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e", key1)

key3 = xor("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1", key2)

key4 = xor(xor(key1, key2), key3)

code = xor("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf", key4)


print("key2 {}".format(key2))
print("key3 {}".format(key3))
print("key4 {}".format(key4))
print("code {}".format(unhexlify(code)))