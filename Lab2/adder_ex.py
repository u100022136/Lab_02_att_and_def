from pwn import *
r = process('./adder')
r.sendline('1\n1\n1335')
r.interactive()
