#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>

int main(int argc, char** argv){
	int sock;
	struct sockaddr_in serv_addr;
	
	sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	if(sock == -1){
		printf("socket error");
	}
	memset(&serv_addr, 0, sizeof(serv_addr));
	serv_addr.sin_family= AF_INET;
	serv_addr.sin_addr.s_addr= inet_addr("127.17.0.5");
	serv_addr.sin_port = htons(3000);
	
	int result = 0;
	result = connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
	if(result == -1){
		printf("connect error");
	}
	
	unsigned char msg[100] = {0x01,2,3,4,5,6,1,2,3,4,2,1,2,3,0x0c};
	
	while(1){
		printf("send : ");
		
		write(sock, msg, 15);
		sleep(1);
	}
	
	close(sock);
	return 0;
}