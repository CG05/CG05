#include <stdio.h>
#include <string.h>

void _strcpy(char *str, char *cpy);
char *strcpy(char *dest, const char *src);
int _strcmp(const char *s1, const char *s2);

int main(){
	char str_c[20] = "hello world\n";
	char str[20] = "good job\n";

	printf("str : %s",str);

	_strcpy(str, str_c);

	printf("str : %s",str);

	char src[20] = "hello world\n";
	char dest[20] = "good job\n";

	printf("dest : %s", dest);

	strcpy(dest, src);

	printf("dest : %s", dest);

	return 0;
}

void _strcpy(char *str, char *cpy){
	int i = 0;
	do{
		char *temp = str + i;
		*temp = *cpy;
		i++;
	}while(*cpy++);
	
}

char *strcpy(char *dest, const char *src){
	while(*src){
		*dest++ = *src++;	
	}
	return dest;
}

