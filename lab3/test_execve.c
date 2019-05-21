#include <stdio.h>

int main() {
	char* argv[] = {"/bin/cat", "/home/level3A/.pass", '\0'};
	execve("/bin/cat", argv, 0);
}
