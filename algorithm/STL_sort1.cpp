#include <iostream>
#include <algorithm>

using namespace std;

class Student {
	public:
		string name;
		int score;
		Student(string name, int score){
			this->name = name;
			this->score = score;
		}
		
		bool operator<(Student &student) {
			return this->score < student.score;
		}
};


int main(void){
	Student students[] = {
		Student("나동빈", 90),
		Student("이상욱", 93),
		Student("박한울", 97),
		Student("강종구", 87),
		Student("이태일", 92)
	};
	sort(students, students + 5, compare);
	for(int i = 0; i < 5; i++){
		cout << students[i].name << ' ';
	}
	
	return 0;
}