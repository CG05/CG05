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

#define IP_ADDR "172.17.0.37"
#define PORT_NUM 8080
#define ERROR_NEGATIVE -1
#define BACKLOG_LENGTH 2048
#define MAX_CLIENT_NUM 10

using namespace std;

struct sockaddr_in serverAddr;
struct sockaddr_in clientAddr;

unsigned int listClient[MAX_CLIENT_NUM];
int countClient = 0;

void acceptClient(int serverSocket);
void msgExchanger(unsigned int clientSocket, int numClient);
void deleteClient(int numClient);

int settingServerSocket();
int bindServerSocket(int serverSocket);
void bindErrorHandler(int bindResult);
int listenClientSocket(int serverSocket);
void listenErrorHandler(int listenResult);
void noticeSetupCompleted();
int connectedClient(int serverSocket);
void updateListClient(int clientSocket);
void noticeNewConnectedClient(int clientSocket);
void renderListClient();
void createUserThread(int clientSocket, int countClient);
string getSpeaker(int clientSocket);
void loopExchanging(int clientSocket, string speaker, int numClient);
string getMsgFrom(int clientSocket, int numClient);
bool isClosed(int msgLength, char* c_msg);
string completeSendMsg(string speaker, string msg);
void deleteClient(int numClient);
void sendToAll(string sendMsg);
void sendErrorHandler(int sendResult, int i);



int main(int argc, char** argv){
	
	int serverSocket;
	serverSocket = settingServerSocket();
	
	int bindResult;
	bindResult = bindServerSocket(serverSocket);
	bindErrorHandler(bindResult);
	
	int listenResult;
	listenResult = listenClientSocket(serverSocket);
	listenErrorHandler(listenResult);
	
	noticeSetupCompleted();
	
	acceptClient(serverSocket);
	
	return 0;
}



void acceptClient(int serverSocket){

	while(true){
		
		int clientSocket;
		clientSocket = connectedClient(serverSocket);
		
		updateListClient(clientSocket);
		noticeNewConnectedClient(clientSocket);
		renderListClient();
		
		createUserThread(clientSocket, countClient);
	}
	
	return;
}

void msgExchanger(unsigned int clientSocket, int numClient){
	string speaker;
	speaker = getSpeaker(clientSocket);
	
	loopExchanging(clientSocket, speaker, numClient);
	
	close(clientSocket);
	
	return;
}

int settingServerSocket(){
	int serverSocket;
	serverSocket = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	
	serverAddr.sin_family = AF_INET;
	serverAddr.sin_addr.s_addr = htonl(INADDR_ANY);
	serverAddr.sin_port = htons(PORT_NUM);
	
	return serverSocket;
}

int bindServerSocket(int serverSocket){
	return bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr));
}

void bindErrorHandler(int bindResult){
	if(bindResult == ERROR_NEGATIVE){
		perror("bind error\n");
	}
	cout << "bind success\n";
	
	return;
}

int listenClientSocket(int serverSocket){
	return listen(serverSocket, BACKLOG_LENGTH);
}

void listenErrorHandler(int listenResult){
	if(listenResult == ERROR_NEGATIVE){
		perror("listen error\n");
	}
	cout << "listen success\n";

	return;
}

void noticeSetupCompleted(){
	cout << IP_ADDR << " : " << PORT_NUM << " Server Setup\n" << endl;
	
	return;
}

int connectedClient(int serverSocket){
	unsigned int clientAddrSize = sizeof(clientAddr);
	int clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &clientAddrSize);
	
	return clientSocket;
}

void updateListClient(int clientSocket){
	listClient[countClient] = clientSocket;
	countClient++;
	
	return;
}

void noticeNewConnectedClient(int clientSocket){
	cout << "Client" << clientSocket << " is connected" << endl;
	
	return;
}

void renderListClient(){
	cout << "Client list : [ ";
	for(int i = 0;i<countClient;i++){
		cout << "Client" << listClient[i] << ", ";
	}
	cout << " ]\n";
	
	return;
}

void createUserThread(int clientSocket, int countClient){
	thread userThread(msgExchanger, clientSocket, countClient);
	userThread.detach();
	
	return;
}

string getSpeaker(int clientSocket){
	char c_id[BACKLOG_LENGTH];
	int idLength;
	
	idLength = read(clientSocket, (char*)c_id, sizeof(c_id));
	
	string id(c_id);
	string speaker;
	speaker = "< " + id + " >";
	
	return speaker;
}

void loopExchanging(int clientSocket, string speaker, int numClient){
	char c_msg[BACKLOG_LENGTH];
	string msg;
	
	while(true){
		msg = getMsgFrom(clientSocket, numClient);
		
		if(msg == "closed"){
			break;
		}
		
		string sendMsg;
		sendMsg = completeSendMsg(speaker, msg);

		sendToAll(sendMsg);
	}
	
	return;
}

string getMsgFrom(int clientSocket, int numClient){
	char c_msg[BACKLOG_LENGTH];
	int msgLength = read(clientSocket, (char*)c_msg, sizeof(c_msg));
	
	if(isClosed(msgLength, c_msg)){
		deleteClient(numClient);
		renderListClient();
		return "closed";
	}
	
	string msg(c_msg);

	return msg;
}

bool isClosed(int msgLength, char* c_msg){
	return msgLength == ERROR_NEGATIVE || strcmp(c_msg, " : exit") == 0;
}

string completeSendMsg(string speaker, string msg){
	string sendMsg = speaker + msg;
	cout << sendMsg << endl;
	
	return sendMsg;
}

void sendToAll(string sendMsg){
	for(int i = 0; i < countClient; i++){
		int sendResult = write(listClient[i], (char*)sendMsg.c_str(), sizeof(sendMsg) + 1);
		
		sendErrorHandler(sendResult, i);
	}
	
	return;
}

void sendErrorHandler(int sendResult, int i){
	if(sendResult == ERROR_NEGATIVE){
		cout << "Failed send to Client" << listClient[i] << endl;	
	}
	
	return;
}

void deleteClient(int numClient){
	for(int i = numClient - 1;i < 10;i++){
		listClient[i - 1] = listClient[i]; 
	}
	listClient[9] = 0;
	countClient--;

	
	return;
}