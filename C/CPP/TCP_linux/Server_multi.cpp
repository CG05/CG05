#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>

#define CLNT_MAX 10
#define PORT_NUM 3000
#define BLOG_LEN 5
#define BUFF_LEN 200

int g_clnt_socks[CLNT_MAX];
int g_clnt_count = 0;

void* clnt_connection(void* arg);

int main(int argc, char** argv){
	
	int serv_sock;
	int clnt_sock;
	
	pthread_t t_thread;
	
	serv_sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	
	struct sockaddr_in serv_addr;
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	serv_addr.sin_port = htons(PORT_NUM);
	
	int result = 0;
	result = bind(serv_sock
				  , (struct sockaddr *)&serv_addr
				  , sizeof(serv_addr));
	if(result == -1){
		printf("bind error\n");
	}
	
	result = listen(serv_sock, BLOG_LEN);
	if(result == -1){
		printf("listen error\n");
	}
	long int serv_ip =serv_addr.sin_addr.s_addr;
	printf("172.17.0.7 : %d Server Setup\n", PORT_NUM);
	
	struct sockaddr_in clnt_addr;
	unsigned int clnt_addr_size;
	
	char buff[BUFF_LEN];
	int recv_len = 0;

	while(1){
		clnt_addr_size = sizeof(clnt_addr);
		
		clnt_sock = accept(serv_sock
						   , (struct sockaddr *)&clnt_addr
						   , &clnt_addr_size);
		
		pthread_create(&t_thread, NULL, clnt_connection, (void*)clnt_sock);
		g_clnt_socks[g_clnt_count++] = clnt_sock;
		
	}
	
}

void* clnt_connection(void* arg){
	int clnt_sock = (intptr_t)arg;
	int str_len = 0;
	
	char msg[BUFF_LEN];
	int i;
	
	while(1){
		str_len = read(clnt_sock, msg, sizeof(msg));
		if(str_len == -1){
			printf("clnt[%d] close\n", clnt_sock);
			break;
		}
		
		printf("%s\n", msg);
	}
	
	close(clnt_sock);
	pthread_exit(0);
	return NULL;
}
