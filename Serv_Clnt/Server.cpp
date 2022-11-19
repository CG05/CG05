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

#define IP_ADDR "172.17.0.16"
#define PORT_NUM 8080
#define ERROR_NEGATIVE -1
#define BACKLOG_LENGTH 2048
#define MAX_CLIENT_NUM 10

using namespace std;

struct sockaddr_in serverAddr;
struct sockaddr_in clientAddr;

unsigned int listClient[MAX_CLIENT_NUM];
int countClient = 0;

void* acceptClient(int _serverSocket);
void* msgExchanger(unsigned int _clientSocket, int numClient);
void* deleteClient(int numClient);


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

void* acceptClient(int _serverSocket){

	while(true){
		unsigned int clientAddrSize = sizeof(clientAddr);
		
		int clientSocket = accept(_serverSocket, (struct sockaddr*)&clientAddr, &clientAddrSize);
		listClient[countClient] = clientSocket;
		countClient++;
		cout << "Client" << countClient << " is connected" << endl;
		cout << "Client list : [ ";
		for(int i = 0;i<countClient;i++){
			cout << "Client" << listClient[i] << ", ";
		}
		cout << " ]\n";

		thread userThread(msgExchanger, clientSocket, countClient);
		userThread.detach();

	}
	
	return NULL;
}

void* msgExchanger(unsigned int _clientSocket, int numClient){
	char c_msg[BACKLOG_LENGTH];
	char c_id[BACKLOG_LENGTH];
	int idLength = read(_clientSocket, (char*)c_id, sizeof(c_id));
	string speaker;
	string id(c_id);
	speaker = "< " + id + " >";
	
	string msg;
	while(true){
		int msgLength = read(_clientSocket, (char*)c_msg, sizeof(c_msg));
		msg = c_msg;
		
		if(msgLength == ERROR_NEGATIVE || strcmp(c_msg, " : exit") == 0){
			cout << speaker << " is closed" << endl;
			deleteClient(numClient);
			countClient--;
			cout << "Client list : [ ";
			for(int i = 0;i<countClient;i++){
				cout << "Client" << listClient[i] << ", ";
			}
			cout << " ]\n";
			break;
		}
		string sendMsg = speaker + msg;
		cout << sendMsg << endl;

		for(int i = 0; i < countClient; i++){
			int sendResult = write(listClient[i], (char*)sendMsg.c_str(), sizeof(sendMsg) + 1);
			if(sendResult == ERROR_NEGATIVE){
				int sendFailedClient = i + 1;
				cout << "Failed send to Client" + to_string(sendFailedClient) + "\n" + "Retrying...";
				i--;
				
			}
		}
	}
	
	close(_clientSocket);
	
	return NULL;
}

void* deleteClient(int numClient){
	if(numClient < 10){
		listClient[numClient - 1] = listClient[numClient]; 
	}else{
		listClient[numClient - 1] = 0;
	}
	
	return NULL;
}