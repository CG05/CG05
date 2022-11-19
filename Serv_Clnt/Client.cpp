#include <iostream>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <thread>

#define IP_ADDR "172.17.0.16"
#define PORT_NUM 8080
#define ERROR_NEGATIVE -1
#define BACKLOG_LENGTH 2048

using namespace std;

struct sockaddr_in serv_addr;

bool isSending = false;
bool isRecving = false;

void* sendMsg(int clientSocket, char* c_id);
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
	
	
	thread sendThread(sendMsg, clientSocket, id);
	sendThread.detach();
	thread recvThread(recvMsg, clientSocket);
	recvThread.detach();
	isRecving = true;
	isSending = true;
	
	while(isSending && isRecving){
		//sending, recieving
	}
	
	cout << "Chat is closing. Bye Bye\n";
	return 0;
}

void* sendMsg(int clientSocket, char* c_id){
	string id(c_id);
	cout << "Server is connected. Enjoy your chatting, < " + id + " >!!\n";
	
	string msg;
	int sendResult = write(clientSocket, c_id, sizeof(c_id) + 1);
	if(sendResult == ERROR_NEGATIVE){
		cout << " connect is missing\n";
		isSending = false;
		return NULL;
	}
	
	msg = " : hello world\n";
	sendResult = write(clientSocket, (char*)msg.c_str(), sizeof(msg) + 1);
	if(sendResult == ERROR_NEGATIVE){
		cout << " connect is missing\n";
		isSending = false;
		return NULL;
	}
	
	while(true){
		getline(cin, msg);
		
		msg = " : " + msg;
		sendResult = write(clientSocket, (char*)msg.c_str(), sizeof(msg) + 1);

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
		cout << msg << endl;
		
	}
	
	close(clientSocket);
	return NULL;
}