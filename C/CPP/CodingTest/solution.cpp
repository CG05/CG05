#include <stdio.h>
#include <string>
#include <cstring>
#include <iostream>
#include <vector>
#include <cctype>

using namespace std;

string polynomial;
int nextBlankIndex = 0;
int indexX = 0;

int plusConstant = 0;
int plusCountX = 0;
int minusCountX = 0;
int minusConstant = 0;
int finalCountX = plusCountX - minusCountX;
int finalConstant = plusConstant - minusConstant;

string solution();
int curIndex = 0;
bool isPlus(int index);
// void checkInterval(int index, int *countX, int *constant);
void checkInterval(int index);

int madeNumber(string interval, int digit);
int findBlank(int index);
string getInterval(int startInterval);
int thereIsX(string interval);
bool isFinished(int index);
string makeAnswer(int countX, int constant);
string sign(int integer);

int main(int argc, char** argv){
	cout << "다항식을 입력하세요 : ";
	getline(cin, polynomial);
	string result = solution();
	cout << "다항식 정리 결과 : " << result << endl;
	
	return 0;
}

string solution() {
	polynomial = "+ " + polynomial + " ";
	
	int size = polynomial.size();
	// vector<string> vecPoly;
    
	string answer = "";

	do{
		// if(isPlus(curIndex)){
		// 	checkInterval(curIndex, &plusCountX, &plusConstant);
		// }else{
		// 	checkInterval(curIndex, &minusCountX, &minusConstant);
		// }
		checkInterval(curIndex);
		
		curIndex = nextBlankIndex + 1;
		cout << "current CountX is " << plusCountX << endl;
		cout << "current Constant is " << plusConstant << endl;
	}while(!isFinished(curIndex));
	
   
	answer = makeAnswer(plusCountX, plusConstant);
        
	return answer;
}

bool isPlus(int index){
	return &polynomial[index] == "+";
}

void checkInterval(int index){
	int startInterval = index + 2;
	nextBlankIndex = findBlank(curIndex);
	string interval = getInterval(startInterval);
	indexX = thereIsX(interval);
	if(indexX == -1){
		plusConstant += madeNumber(interval, interval.size());
	}else if(indexX == 0){
		plusCountX++;
	}else{
		plusCountX += madeNumber(interval, interval.size() - 1);
	}
	
}

int madeNumber(string interval, int digit){
	string str_number = interval.substr(0, digit);
	int number = stoi(str_number);
	cout << "made number : " << number << endl;
	
	return number;
}

int findBlank(int index){
	int nextBlankIndex = polynomial.find(" ", index + 2);
	
	return nextBlankIndex;
}

string getInterval(int startInterval){
	string interval = polynomial.substr(startInterval, nextBlankIndex - startInterval);
	
	return interval;
}

int thereIsX(string interval){
	int indexX = interval.find("x");
	
	return indexX;
}

bool isFinished(int index){
	bool result = false;
	if(findBlank(index) == -1){
		result = true;
	}
	
	return result;
}

string makeAnswer(int countX, int constant){
	string answer = "";
	if(sign(countX) == "NORMAL"){
		
			answer.append(to_string(countX));
			answer.append("x");
			if(constant > 0){
				answer.append(" + ");
				answer.append(to_string(constant));
			}else if(constant < 0){
				answer.append(to_string(constant));
			}
	}else if(sign(countX) == "POSITIVE ONE"){
	
			answer.insert(0, "x");
			if(constant > 0){
				answer.append(" + ");
				answer.append(to_string(constant));
			}else if(constant < 0){
				answer.append(to_string(constant));
			}
	}else if(sign(countX) == "ZERO"){
	
			if(constant != 0){
				answer.append(to_string(constant));
			}
	}else if(sign(countX) == "NEGATIVE ONE"){
			answer.insert(0, "- x");
			if(constant > 0){
				answer.append(" + ");
				answer.append(to_string(constant));
			}else if(constant < 0){
				answer.append(to_string(constant));
			}
	}
	
	return answer;
}

string sign(int integer){
	string result = "";
	if(integer == 1){
		result = "POSITIVE ONE";
	}else if(integer == 0){
		result = "ZERO";
	}else if(integer == -1){
		result = "NEGATIVE ONE";
	}else{
		result = "NORMAL";
	}
	
	return result;
}

