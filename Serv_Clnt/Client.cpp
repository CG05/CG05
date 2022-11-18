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
#define PORT_NUM 8080
#define ERROR_NEGATIVE -1
#define BACKLOG_LENGTH 2048

using namespace std;

struct sockaddr_in serv_addr;

bool isSending = false;
bool isRecving = false;

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
	serv_addr.sin_port = htons(PORT_NUM);
	
	int result = 0;
	result = connect(clientSocket, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
	if(result == -1){
		cout << "connect error\n";
	}
	cout << "connect OK\n";
	
	
	thread sendThread(sendMsg, clientSocket);
	sendThread.detach();
	thread recvThread(recvMsg, clientSocket);
	recvThread.detach();
	isRecving = true;
	isSending = true;
	
	while(isSending && isRecving){
		//sending, recieving
	}
	
	return 0;
}

void* sendMsg(int clientSocket){
	string msg;
	
	msg = " : hello world\n";
	cout << "send" << msg;

	int sendResult = write(clientSocket, (char*)msg.c_str(), sizeof(msg));
	if(sendResult == ERROR_NEGATIVE){
		cout << " connect is missing\n";
		isSending = false;
		return NULL;
	}
	cout << "send : ";
	while(true){
		cin >> msg;
		
		msg = " : " + msg;
		sendResult = write(clientSocket, (char*)msg.c_str(), sizeof(msg));

		if(sendResult == ERROR_NEGATIVE){
			cout << " connect is missing\n";
			isSending = false;
			break;
		}
	}
	
	close(clientSocket);
	return NULL;
}
void* recvMsg(int clientSocket){
	char c_msg[BACKLOG_LENGTH];
	string msg;
	
	while(true){
		int msgLength = read(clientSocket, c_msg, sizeof(c_msg));
		msg = c_msg;
		if(msgLength == ERROR_NEGATIVE){
			cout << " connect is missing\n";
			isRecving = false;
			break;
		}else if(msgLength == NULL){
			cout << "EXIT\n";
			isRecving = false;
			break;
		}
		cout << "\n" + msg + "\nsend : ";
		
	}
	
	close(clientSocket);
	return NULL;
}