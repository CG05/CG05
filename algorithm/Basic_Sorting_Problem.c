//https://www.acmicpc.net/problem/2750
//숫자 정렬하기

// #include <stdio.h>

// int array[1001];

// int main(void){
// 	int number, i, j, min, max, index, temp;
// 	scanf("%d", &number);
// 	for(i = 0; i < number; i++){
// 		scanf("%d", &array[i]);
		
// 	}
// 	for(i = 0; i < number; i++){
// 		min = 1001;
// 		for(j = i; j < number; j++){
// 			if(min > array[j]){
// 				min = array[j];
// 				index = j;
// 			}
// 		}
// 		temp = array[i];
// 		array[i] = array[index];
// 		array[index] = temp;
// 	}
	
// 	for(i = 0; i < number;i++){
// 		printf("%d\n", array[i]);
// 	}
	
	
// 	return 0;
// }

//https://www.acmicpc.net/problem/2752
//세 수 정렬하기

// #include <stdio.h>

// int array[3];

// int main(void){
// 	int i, j, min, max, index, temp;
	
// 	for(i = 0; i < 3; i++){
// 		scanf("%d", &array[i]);
		
// 	}
// 	for(i = 0; i < 3; i++){
// 		min = 1000001;
// 		for(j = i; j < 3; j++){
// 			if(min > array[j]){
// 				min = array[j];
// 				index = j;
// 			}
// 		}
// 		temp = array[i];
// 		array[i] = array[index];
// 		array[index] = temp;
// 	}
	
// 	for(i = 0; i < 3;i++){
// 		printf("%d ", array[i]);
// 	}
	
	
// 	return 0;
// }

//https://www.acmicpc.net/problem/2751
//100만 개 정렬하기

#include <stdio.h>
#include <algorithm>

int number, data[1000001];

void quickSort(int *data, int start, int end){
	if(start >= end){
		return;
	}
	int key = start;
	int i = start + 1;
	int j = end;
	int temp;
	
	while(i <= j){
		while(data[i] <= data[key]){
			i++;
		}
		while(data[j] >= data[key] && j > start){
			j--;
		}
		if(i > j){
			temp = data[j];
			data[j] = data[key];
			data[key] = temp;
		}else{
			temp = data[i];
			data[i] = data[j];
			data[j] = temp;
		}
		
	}
	
	quickSort(data, start, j - 1);
	quickSort(data, j + 1, end);
	
}

int main(void){
	scanf("%d", &number);
    
	for(int i = 0; i < number; i++){
		scanf("%d", &data[i]);
		
	}
	
	std::random_shuffle(data, data + number);
	//최악의 시간복잡도를 피하기 위한 강제 셔플
	
	quickSort(data, 0, number - 1);
	
	for(int i = 0; i < number;i++){
		printf("%d\n", data[i]);
	}
	
	
	return 0;
}