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
#define EXIT_CODE "exit"

int SetTCPClient(char server_ip, short pnum, int blog);
void MsgLoop(int sock);
void DoIt(int dosock);

struct SOCKADDR_IN {
    short            sin_family;   // e.g. AF_INET
    unsigned short   sin_port;     // e.g. htons(3490)
    struct in_addr   sin_addr;     // see struct in_addr, below
    char             sin_zero[8];  // zero this if you want to
};

int main() {
	char server_ip[40] = "";
	cout << "Server IP : ";
	cin.getline(server_ip, sizeof(server_ip));
	
	int sock = SetTCPClient(server_ip, PORT_NUM, MAX_MSG_LEN);
	MsgLoop(sock);
	
}

int SetTCPClient(char server_ip, short pnum, int blog){
	int sock;
	sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	SOCKADDR_IN  servaddr = {0};
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr = htonl(server_ip);
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
	
	printf("%s : %d Connected\n",ntohl(servaddr.sin_addr), pnum);
	
	return sock;
}

void MsgLoop(SOCKET sock){
	char msg[MAX_MSG_LEN] = "";
	while(true){
		cin.getline(msg, MAX_MSG_LEN);
		send(sock, msg, sizeof(msg));
		if(!strcmp(msg, EXIT_CODE)){
			break;
		}
		recv(sock, msg, sizeof(msg),0);
		cout << "수신 : " << msg << endl;
	}
	close(sock);
}
