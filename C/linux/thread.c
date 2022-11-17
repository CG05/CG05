#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

int a = 0;
pthread_mutex_t mutex;
void * thread1(void * arg);

int main(){
	pthread_t s_thread[2];
	int id1 = 77;
	int id2 = 88;	
	
	pthread_mutex_init(&mutex, NULL);
	
	pthread_create(&s_thread[0], NULL, thread1, (void *)id1);
	pthread_create(&s_thread[1], NULL, thread1, (void *)id2);

	
	pthread_join(s_thread[0], NULL);
	pthread_join(s_thread[1], NULL);

	
	return 0;
	
}

void * thread1(void * arg){
	printf("arg : %d\n", (int)arg);
	while(1){
		pthread_mutex_lock(&mutex);
		printf("thread1 a[%d]\n", ++a);
		pthread_mutex_unlock(&mutex);

		sleep(2);
	}
	return NULL;
}
