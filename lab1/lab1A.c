
char* username = "admins";

int auth(char* username, int serial){

	username[strcspn(*username, "\n")] = '\0';
	int username_len = strnlen(*username, 32);

	if (username_len <= 5) {
		return 1;
	}

	int hash = (username[3] ^ 0x1337) + 0x5eeded;
	int i = 0;

	while (i < username_len) {
		if (username[i] <= 31) {
			return 1;
		}
		int x = ((int)username[i] ^ hash);
		int y = x - (x * 0x88233b2b) % 0x100000000;
		hash = x - ((((x - y) >> 1) + y) >> 10) * 0x539;
		i++;
	}
	
	if (hash == serial)
		return 0;
	else
		return 1;

}
