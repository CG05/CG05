#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>


// void* send_message(void* arg);
// void* recv_message(void* arg);


int main(int argc, char** argv){
	int sock;
	struct sockaddr_in serv_addr;
	pthread_t snd_thread, rcv_thread;
	void* thread_result;
	
	char id[100];
	strcpy(id, argv[1]);
	printf("id : %s\n", id);
	
	sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	if(sock == -1){
		printf("socket error\n");
	}else{
		printf("socket OK\n");

	}
	memset(&serv_addr, 0, sizeof(serv_addr));
	serv_addr.sin_family= AF_INET;
	serv_addr.sin_addr.s_addr= inet_addr("172.17.0.7");
	serv_addr.sin_port = htons(3000);
	
	int result = 0;
	result = connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
	if(result == -1){
		printf("connect error\n");
	}
	printf("connect OK\n");
	
	// pthread_create(&snd_thread, NULL, send_message, (void*)sock);
	// pthread_create(&rcv_thread, NULL, recv_message, (void*)sock);
	
	// pthread_join(snd_thread, &thread_result);
	// pthread_join(rcv_thread, &thread_result);


	char msg[200];
	
	sprintf(msg, "[%s] : hello world", id);
	printf("while before\n");
	
	while(1){
		printf("send : %s\n", msg);
		
		write(sock, msg, strlen(msg)+1);
		sleep(1);
	}
	printf("while end\n");
	
	close(sock);
	return 0;
}