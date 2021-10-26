from pwn import *
payload = chr(0x67)+chr(0x33)+chr(0x7a)+chr(0x6b)+chr(0x6d)

print(payload)
r = process(['./ezreverse',payload])
r.interactive()

