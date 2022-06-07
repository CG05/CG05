#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct data{
	int num;
	char name[20];

	struct data *next;
}data;

data *g_head = NULL;
data *g_tail = NULL;

int insert(int num, char *name);
void printAll();
data *stack_pop();
data *dequeue();
data *find(int num);

int main(void){

	for(int i = 0;i < 10; i++){
		char name[20];
		sprintf(name, "test%d", i);
		insert(i, name);
	}
	int index = 0;

	printf("What index you want to find?");
	scanf("%d", &index);
	if(find(index) == NULL){
		return -1;
	}else{
		printf("*******************\n");
		printf("Found\n num : %d\n name: %s\n", find(index) -> num, find(index) -> name);
		printf("*******************\n");
	}

	return 0;
}

int insert(int num, char *name){
	data *node = malloc(sizeof(data));
	node -> num = num;
	if(name != NULL){
		strcpy(node -> name, name);
	}

	if(g_head == NULL){
		g_head = node;
		g_tail = node;
		node -> next = NULL;
		return 1;
	}else{
		data *temp = g_head;
		
		while(temp -> next){
			temp = temp -> next;
		}
		temp -> next = node;
		g_tail = node;
	}

	return 0;
}

void printAll(){
	if(g_head == NULL){
		printf("=============\n");
		printf("There is Nothing Left.\n");
		printf("=============\n");
		return;
	}
	data *temp = g_head;
			
	do{
		printf("=============\n");
		printf("num: %d\n", temp -> num);
		printf("name: %s\n", temp -> name);
		printf("=============\n");
		temp = temp -> next;
	}while(temp);
}

data *stack_pop(){
	if(g_head == NULL){
		return NULL;
	}
	
	data *node = g_tail;

	data *temp = g_head;
	data *before = NULL;
		
	while(temp -> next){
		before = temp;
		temp = temp -> next;
	}
	
	g_tail = before;
	if(before != NULL){
		before -> next = NULL;
	}
	if(g_tail == NULL){
		g_head = NULL;
	}

	return node;
}

data *dequeue(){
	if(g_head == NULL){
		return NULL;
	}
	
	data *node = g_head;
	g_head = node -> next;

	if(g_head == NULL){
		g_tail = NULL;
	}

	return node;
}

data *find(int num){
	if(g_head == NULL){
		printf("no data in here\n");
		return NULL;
	}
	data *temp = g_head;
	while(temp){
		if(temp -> num == num){
			return temp;
		}
		temp = temp -> next;
	}
	printf("Index Error: Not Exist");
	return NULL;
}