#include <string>
#include <cstring>
#include <iostream>
#include <vector>
#include <cctype>

using namespace std;

string polynomial;
string solution(string polynomial);
void countOrConst(int index);
string makeAnswer(int countX, int constant);

int main(int argc, char** argv){
	char poly_c[50];
	strcpy(poly_c, argv[1]);
	cout << solution(poly_c);
	
	return 0;
}

string solution(string polynomial) {
    int size = polynomial.size();
    vector<string> vecPoly;
    int countX = 0;
    int constant = 0;
	string answer = "";
	
	countOrConst(0);
	
	int indexBlank = 0;
	while(indexBlank > -1){
		countOrConst(indexBlank + 1);
		indexBlank = polynomial.find(" ", indexBlank);
	}
	
    
    answer = makeAnswer(countX, constant);
        
    return answer;
}

void countOrConst(int index){
	if(polynomial[index] == "x"){
		countX ++;
	}else if(isdigit(polynomial[index])){
		if(polynomial[index + 1] == "x"){
			countX += polynomial[index];
		}else{
			constant += polynomial[index];
		}
	}
}

string makeAnswer(int countX, int constant){
	string answer = "";
	if(countX > 0){
		if(countX > 1){
			answer.insert(0,to_string(countX));
			answer.insert(1, "x");
		}
		answer.insert(0, "x");
	}
	
	if(constant > 0){
		answer.append(" + ");
		answer.append(to_string(constant));

	}
	
	return answer;
}

