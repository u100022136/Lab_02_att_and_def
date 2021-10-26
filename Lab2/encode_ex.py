from pwn import *

r = process('./encode')

#9cac105bc36a45(hex)-->47bcc14f9b7a86(17base)

password = [0]*27+[12,0,10,4,2,7,17,19,14,8,13,19]

code = ''

for i in password:
	code = code + chr(65+i)

r.sendline(code)

r.interactive()
