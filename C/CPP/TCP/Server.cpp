#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "unistd.h"
#include "sys/types.h"
#include "sys/socket.h"
#include "netinet/in.h"

#define NO_REQUEST -1
#define PORT_NUM 10200
#define MAX_MSG_LEN 256

int SetTCPServer(short pnum, int blog);
void AcceptLoop(int sock);
void DoIt(int dosock);

struct SOCKADDR_IN {
    short            sin_family;   // e.g. AF_INET
    unsigned short   sin_port;     // e.g. htons(3490)
    struct in_addr   sin_addr;     // see struct in_addr, below
    char             sin_zero[8];  // zero this if you want to
};

int main() {
	
	int sock = SetTCPServer(PORT_NUM, MAX_MSG_LEN);
	AcceptLoop(sock);
	close(sock);

}

int SetTCPServer(short pnum, int blog){
	int sock;
	sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	SOCKADDR_IN  servaddr = {0};
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr = htonl(INADDR_ANY);
	servaddr.sin_port = htons(pnum);
	
	int request = 0;
	
	request = bind(sock, (struct SOCKADDR_IN*)&servaddr, sizeof(servaddr));
	if(request == NO_REQUEST){
		return NO_REQUEST;
	}
	
	request = listen(sock, blog);
	if(request == NO_REQUEST){
		return NO_REQUEST;
	}
	
	printf("%s : %d Setup\n",ntohl(servaddr.sin_addr), pnum);
	
	return sock;
}

void AcceptLoop(int sock){
	int dosock;
	SOCKADDR_IN cliaddr={0};
	int addrLen = sizeof(cliaddr);
	while(true){
		dosock = accept(sock, (struct SOCKADDR_IN*)&cliaddr, &addrLen);
		if(dosock == NO_REQUEST){
			perror("Accept Disable");
			break;
		}
		printf("%s : %d의 연결 요청 수락\n"
			   , ntohl(cliaddr.sin_addr)
			   , ntohs(cliaddr.sin_port));
		DoIt(dosock);
	}
}

void DoIt(int dosock){
	char msg[MAX_MSG_LEN] = "";
	while(recv(dosock, msg, sizeof(msg),0) > 0){
		printf("recv : %s\n", msg);
		send(dosock, msg, sizeof(msg), 0);
	}
	close(dosock);

}
