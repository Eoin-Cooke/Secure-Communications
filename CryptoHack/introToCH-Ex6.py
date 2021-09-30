from Crypto.Util.number import *

longNumber = 1515195063862318899931685488813747395775516287289682636499965282714637259206269

byte = long_to_bytes(longNumber)

print(byte)

#for some reason, this doesn't work. It says that the module 
#Cryptodome.Util.number doesn't exist even though I have 
#Crypotdome installed. I even reinstalled it and it still doesn't work.