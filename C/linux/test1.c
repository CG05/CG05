#include <stdio.h>

int main(void){
	char str[100] = "Hello world\n";
	char *pstr = str;
	do{
		putchar(*pstr);
	}while(*pstr++);

	return 0;
}