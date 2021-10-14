from pwn import xor

hexcode = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(256):

    code = xor(hexcode, i)

    if b"crypto" in code:

        print(code)