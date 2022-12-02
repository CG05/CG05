#include <iostream>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <thread>

#define IP_ADDR "172.17.0.37"
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
	
	char id[BACKLOG_LENGTH];
	strcpy(id, argv[1]);
	printf("id : %s\n", id);
	//printMyId(argv);
	
	int clientSocket;
	clientSocket = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	//clientSocket = createClientSocket();
	if(clientSocket == ERROR_NEGATIVE){
		cout << "socket error\n";
	}else{
		cout << "socket OK\n";
	}
	//socketErrorHandler(clientSocket);
	
	memset(&serv_addr, 0, sizeof(serv_addr));
	serv_addr.sin_family= AF_INET;
	serv_addr.sin_addr.s_addr= inet_addr(IP_ADDR);
	serv_addr.sin_port = htons(PORT_NUM);
	//clientSocket = settingClientSocket();
	
	int connectResult = 0;
	connectResult = connect(clientSocket, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
	//connectTo(clientSocket);
	
	if(connectResult == ERROR_NEGATIVE){
		cout << "connect error\n";
	}
	cout << "connect OK\n";
	//connectErrorHandler(connectResult);
	
	
	thread sendThread(sendMsg, clientSocket, id);
	sendThread.detach();
	thread recvThread(recvMsg, clientSocket);
	recvThread.detach();	
	isRecving = true;
	isSending = true;
	//startCommunicate(clientSocket, id);

	
	while(isSending && isRecving/**isCommunicating*/){
		//sending, recieving
	}
	
	cout << "Chat is closing. Bye Bye\n";
	return 0;
}

void* sendMsg(int clientSocket, char* c_id){
	cout << "Server is connected. Enjoy your chatting, < " << c_id << " >!!\n";
	//renderGreeting(c_id);
	
	string msg;
	int sendResult = write(clientSocket, c_id, sizeof(c_id) + 1);
	//sendMsgTo(clientSocket, c_id);

	if(sendResult == ERROR_NEGATIVE){
		cout << " connect is missing\n";
		isSending = false;
		return NULL;
	}
	//sendErrorHandler(sendResult);
	
	msg = " : hello world\n";
	sendResult = write(clientSocket, (char*)msg.c_str(), sizeof(msg) + 1);
	//sendMsgTo(clientSocket, msg);

	if(sendResult == ERROR_NEGATIVE){
		cout << " connect is missing\n";
		isSending = false;
		return NULL;
	}
	//sendErrorHandler(sendResult);
	//sendHelloMsg(clientSocket);
	
	while(true){
		getline(cin, msg);
		msg = " : " + msg;
		//msg = getMsgLine();
		
		sendResult = write(clientSocket, (char*)msg.c_str(), sizeof(msg) + 1);
		//sendMsgTo(clientSocket, msg);


		if(sendResult == ERROR_NEGATIVE){
			cout << " connect is missing\n";
			isSending = false;
			break;
		}
		//sendErrorHandler(sendResult);

	}
	//loopSendingMsg(clientSocket);
	
	close(clientSocket);
	return NULL;
}
void* recvMsg(int clientSocket){
	char c_msg[BACKLOG_LENGTH];
	string msg;
	
	while(true){
		int msgLength = read(clientSocket, c_msg, sizeof(c_msg));
		msg = c_msg;
		//recvMsgFrom(clientSocket, msg);
		
		if(msgLength == ERROR_NEGATIVE){
			cout << " connect is missing\n";
			isRecving = false;
			break;
		}else if(msgLength == NULL){
			cout << "EXIT\n";
			isRecving = false;
			break;
		}
		//RecvErrorHandler(msgLength);
		
		cout << msg << endl;
		
	}
	//loopRecvingMsg(clientSocket);
	
	close(clientSocket);
	return NULL;
}