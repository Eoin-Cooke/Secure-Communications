from pwn import xor

hexcode = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

print(xor(hexcode, "myXORkey".encode()))

#i used print(xor(hexcode, "crypto{".encode())) to figure out the myXORkey part