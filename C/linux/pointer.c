#include <stdio.h>

int main(void){

	int a;
	char *b;
	float *c;
	double *d;
	short *e;

	printf("%u", sizeof(a));
	printf("%u", sizeof(b));
	printf("%u", sizeof(c));
	printf("%u", sizeof(d));
	printf("%u", sizeof(e));
	
	return 0;
}
