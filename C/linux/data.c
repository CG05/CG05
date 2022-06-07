#include <stdio.h>
#define MAX 200

int g_h_total = 0;
void add_h(int *h_num);
void print_all(int *h_num);

int main(void){
	int h_num[MAX] = {0,};

	for(int i = 0; i < MAX; i++){
		add_h(h_num);
		
	}


	print_all(h_num);

	
	
	return 0;
	
}

void add_h(int *h_num){
	h_num[g_h_total ++] = (g_h_total + 1) * 2;
}

void print_all(int *h_num){
	int i = 0;
	while(*(h_num + i)){
		printf("%d : %d\n", i, *(h_num+i));
		i++;
		if(i>= MAX){
			break;
		}
	}
}