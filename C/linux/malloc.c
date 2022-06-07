#include <stdio.h>
#include <stdlib.h>

int main(void){
	int *h_num;

	h_num = (int *)malloc(sizeof(int));
	//힙 영역의 특정한 주소에 직접 사이즈 만큼의 공간을 창출 -> 이후 free를 통해 공간을 반환해줘야 한다.
	//그렇지 않으면 memory leak이 발생함.

	*h_num = 4;

	printf("%d\n", *h_num);


	return 0;


}
