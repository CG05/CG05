#include <iostream>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <thread>

#define IP_ADDR "172.17.0.2"
#define PORT_NUM 3000
#define ERROR_NEGATIVE -1
#define BACKLOG_LENGTH 2048

using namespace std;

struct sockaddr_in serv_addr;

void* sendMsg(int clientSocket);
void* recvMsg(int clientSocket);

int main(int argc, char** argv){
	int clientSocket;
	
	char id[100];
	strcpy(id, argv[1]);
	printf("id : %s\n", id);
	
	clientSocket = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	if(clientSocket == -1){
		cout << "socket error\n";
	}else{
		cout << "socket OK\n";

	}
	memset(&serv_addr, 0, sizeof(serv_addr));
	serv_addr.sin_family= AF_INET;
	serv_addr.sin_addr.s_addr= inet_addr(IP_ADDR);
	serv_addr.sin_port = htons(3000);
	
	int result = 0;
	result = connect(clientSocket, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
	if(result == -1){
		cout << "connect error\n";
	}
	cout << "connect OK\n";
	
	
	thread sendThread(sendMsg, clientSocket);
	thread recvThread(recvMsg, clientSocket);
	//sending, recieving
}

void* sendMsg(int clientSocket){
	string msg;
	string id;
	cout << "enter your id : ";
	cin >> id;
	
	msg = " : hello world\n";
	write(clientSocket, (char*)msg.c_str(), sizeof(msg)+1);
	
	while(true){
		cout << "send : ";
		cin >> msg;
		
		msg = " : " + msg;
		
		int sendResult = write(clientSocket, (char*)msg.c_str(), sizeof(msg)+1);
		if(sendResult == ERROR_NEGATIVE){
			cout << " connect is missing\n";
			break;
		}
	}
	
	close(clientSocket);
	return NULL;
}
void* recvMsg(int clientSocket){
	string msg;
	
	while(true){
		int msgLength = read(clientSocket, (char*)msg.c_str(), sizeof(msg));
		if(msgLength == ERROR_NEGATIVE){
			cout << " connect is missing\n";
			break;
		}
		cout << msg << endl;
	}
	
	close(clientSocket);
	return NULL;
}