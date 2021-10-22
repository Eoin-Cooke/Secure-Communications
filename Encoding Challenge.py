from pwn import * 
import json
from Crypto.Util.number import *
import base64
import codecs
import random
from binascii import unhexlify


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def codeString(i):
    output = ""
    return(output.join(i))

for i in range(0,101):
    received = json_recv()
    if "code" in received:
        print("code: {}".format(received["code"]))
        

    message = received["encoded"]
    code = received["type"]

    if code == "base64":
        decoded = base64.b64decode(message).decode('utf8').replace("'", '"')
    
    
    elif code == "hex":
        decoded = (unhexlify(message)).decode('utf8').replace("'", '"')
    
    
    elif code == "rot13":
        decoded = codecs.decode(message, 'rot_13')
    
    
    elif code == "bigint":
        decoded = unhexlify(message.replace("0x", "")).decode('utf8').replace("'", '"')
    
    
    elif code == "utf-8":
        decoded = codeString([chr(x) for x in message])

    else:
        print("Error")

    to_send = {
       "decoded": decoded
    }

    json_send(to_send)