#include <stdio.h>

int getPass(char *b)
{

	if (b[0] == 'i') {
	if (b[1] == 'd') {
	if (b[2] == 'a') {
	if (b[3] == '_') {
	if (b[4] == 'i') {
	if (b[5] == 's') {
	if (b[6] == '_') {
	if (b[7] == 'u') {
	if (b[8] == 's') {
	if (b[9] == 'e') {
	if (b[10] == 'f') {
	if (b[11] == 'u') {
	if (b[12] == 'l') {
	if (b[13] == '!') {
		return 1;
	}
	}
	}
	}
	}
	}
	}
	}
	}
	}
	}
	}
	}
	}
	return 0;
}
int main(int argc, char **argv)
{
	char buffer[64];

	printf("Welcome to your crackme problem!\n");
	printf("What is the password?: ");
	scanf("%64s", buffer);

	if (getPass(buffer))
	{
		printf("That is correct! :)\n");
	} else
      printf("That is incorrect! :(\n");
	
    system("pause");
    return 0;
}
