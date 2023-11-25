//3 7 8 1 5 9 6 10 2 4
//pivot1 : 3 -> 3<7:!
//opposite -> 3<4:OK 3>2:!
//3 2 8 1 5 9 6 10 7 4
//3>2:OK 3<8:! ; 3<4:OK ... 3>1:!
//3 2 1 8 5 9 6 10 7 4
//no more ; 3<4:OK ... 3>1:!
//1 2 3. 8 5 9 6 10 7 4 -> pivot1:DONE 
//-> pivot2 : 1 : DONE...pivot3 : 2 : DONE...
//1. 2. 3. 8 5 9 6 10 7 4 -> pivot4 : 8
//...


#include <stdio.h>

int number = 10;
int data[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

void quickSort(int *data, int start, int end){
	if(start >= end){//원소가 1개인 경우
		return;
	}
	
	int key = start;//키는 첫 번째 원소
	int i = start + 1;
	int j = end;
	int temp;
	
	while(i <= j){//엇갈릴 때까지 반복
		while(data[i] <= data[key]){//키 값보다 큰 값을 만날 때까지 반복
			i++;
		}
		while(data[j] >= data[key] && j > start){//키 값보다 작은 값을 만날 때까지 반복
			j--;
		}
		if( i > j){//현재 엇갈린 상태면 키 값과 교체
			temp = data[j];
			data[j] = data[i];
			data[i] = temp;
		}
	}
	
	quickSort(data, start, j - 1);
	quickSort(data, j + 1, end);
}

int main(void){
	int i, j, temp;
	quickSort(data, 0, number - 1);
	
	for(i = 0; i < 10;i++){
		printf("%d ", array[i]);
	}
	return 0;
}