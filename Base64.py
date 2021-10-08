import base64

hex = bytearray.fromhex("72 bc a9 b6 8f c1 6a c7 be eb 8f 84 9d ca 1d 8a 78 3e 8a cf 96 79 bf 92 69 f7 bf")


base = base64.b64encode(hex)

print(base)