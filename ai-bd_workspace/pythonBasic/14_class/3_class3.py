class Student:
    name = input("이름 입력 : ");
    age = input("나이 입력 : ");

    def output(self):
        print(f"{self.name}님의 나이는 {self.age}살 입니다.");

stu = Student();
stu.output();

stu1 = Student();
stu1.output();
