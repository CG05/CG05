#include <stdio.h>
#include <string.h>

typedef struct {
	int s_id;
	char *name;
	
}std;

void std_set(std *st1){
	st1->s_id = 10;
	st1->name = "Chulkyu";

	printf("s_id: %d\n", st1->s_id);
	printf("name: %s\n", st1->name);
	printf("st1: %ld\n", st1);
	printf("pid: %ld\n", &st1->s_id);
	printf("pname: %ld\n", &(*st1).name);
}

int main(void){
	std st;

	printf("st: %ld\n", st);
	printf("&st: %ld\n", &st);
	printf("pid: %ld\n", &st.s_id);
	printf("pname: %ld\n", &st.name);

	
	std_set(&st);
	

	return 0;
}