#include <stdio.h>

void test();
void test2();

int main(void){
	void (*fp)();

	fp = test;
	fp();
	printf("test: %u, &test: %u\n", test, &test);

	fp = test2;
	fp();
	printf("test2: %u, &test2: %u\n", test2, &test2);
	
}

void test(){
	printf("func test\n");
}
void test2(){
	printf("func test2\n");
}