#include <stdio.h>

void swap(int *_a,int *_b);

int main(void){
	int a =3;
	int b =4;

	int *pa = &a;
	int *pb = &b;

	printf("a = %d, b = %d\n", a, b);
	swap(pa, pb);
	printf("a = %d, b = %d\n", a, b);

	return 0;
}

void swap(int *pa, int *pb){
	int temp = *pa;
	*pa = *pb;
	*pb = temp;
}