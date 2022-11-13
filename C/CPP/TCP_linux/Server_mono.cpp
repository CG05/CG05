#include <stdio.h>
#include <stdlib.h>
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

int main(int argc, char** argv){
	
	int serv_sock;
	int clnt_sock;
	serv_sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	
	struct sockaddr_in serv_addr;
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	serv_addr.sin_port = htons(PORT_NUM);
	
	int result = 0;
	result = bind(serv_sock
				  , (struct sockaddr*)&serv_addr
				  , sizeof(serv_addr));
	if(result == -1){
		perror("bind error\n");
	}
	
	result = listen(serv_sock, BLOG_LEN);
	if(result == -1){
		perror("listen error\n");
	}
	
	printf("Server Setup\n");
	
	struct sockaddr_in clnt_addr;
	unsigned int clnt_addr_size;
	
	char buff[BUFF_LEN];
	int recv_len = 0;

	while(1){
		clnt_addr_size = sizeof(clnt_addr);
		
		clnt_sock = accept(serv_sock
						   , (struct sockaddr*)&clnt_addr
						   , &clnt_addr_size);
		
		// g_clnt_socks[g_clnt_count++] = clnt_sock;
		
		recv_len = read(clnt_sock, buff, BUFF_LEN);
		
		printf("recv : ");
		for(int i = 0; i < recv_len; i++){
			printf("%02X", (unsigned char)buff[i]);
		}
		printf("\n");
		
	}
	
}