#include <iostream>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <string>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <thread>

#define IP_ADDR "172.17.0.2"
#define PORT_NUM 8080
#define ERROR_NEGATIVE -1
#define BACKLOG_LENGTH 2048
#define MAX_CLIENT_NUM 10

using namespace std;

struct sockaddr_in serverAddr;
struct sockaddr_in clientAddr;

unsigned int listClient[MAX_CLIENT_NUM];

void* acceptClient(int serverSocket);
void* msgExchanger(unsigned int clientSocket, int clientCount);


int main(int argc, char** argv){
	
	int serverSocket;
	serverSocket = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	
	serverAddr.sin_family = AF_INET;
	serverAddr.sin_addr.s_addr = htonl(INADDR_ANY);
	serverAddr.sin_port = htons(PORT_NUM);
	
	int result;
	result = bind (serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr));
	if(result == ERROR_NEGATIVE){
		perror("bind error\n");
		int bindCount = 1;

		while(result == ERROR_NEGATIVE){
			cout << "bind count : " << bindCount++ << endl;
			result = bind (serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr));
			sleep(1);
		}
		cout << "bind success\n";
	}
	
	result = listen(serverSocket, BACKLOG_LENGTH);
	if(result == ERROR_NEGATIVE){
		perror("listen error\n");
		int listenCount = 1;

		while(result == ERROR_NEGATIVE){
			cout << "listen count : " << listenCount++ << endl;
			result = listen(serverSocket, BACKLOG_LENGTH);
			sleep(1);
		}
		cout << "listen success\n";
	}
	
	cout << IP_ADDR << " : " << PORT_NUM << " Server Setup\n" << endl;
	acceptClient(serverSocket);
	
	return 0;
}

void* acceptClient(int serverSocket){
	
	int countClient = 0;

	while(true){
		unsigned int clientAddrSize = sizeof(clientAddr);
		
		int clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &clientAddrSize);
		listClient[countClient] = clientSocket;
		countClient++;
		cout << "Client" << countClient << " is connected" << endl;

		thread userThread(msgExchanger, clientSocket, countClient);
		userThread.detach();

	}
	
	return NULL;
}

void* msgExchanger(unsigned int clientSocket, int countClient){
	char c_msg[BACKLOG_LENGTH];
	string msg;
	while(true){
		int msgLength = read(clientSocket, (char*)c_msg, sizeof(c_msg));
		msg = c_msg;
		string speaker;
		speaker = "Client" + to_string(countClient);
		
		if(msgLength == ERROR_NEGATIVE || strcmp(c_msg, " : exit") == 0){
			cout << speaker << " is closed" << endl;
			break;
		}
		string sendMsg = speaker + msg;
		cout << sendMsg;

		for(int i = 0; i < countClient; i++){
			write(listClient[i], (char*)sendMsg.c_str(), sizeof(sendMsg));
				
		}
	}
	
	close(clientSocket);
	
	return NULL;
}