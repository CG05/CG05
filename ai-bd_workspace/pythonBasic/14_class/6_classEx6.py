class Student:
    def __init__(self): # 생성자
        self.name = input("이름 입력 : ");
        self.age = input("나이 입력 : ");
    def output(self):
        print(f"{self.name}님의 나이는 {self.age}살 입니다.");
    def __repr__(self) -> str:
        return(self.name);
    # def __str__(self): # 문자열 반환
    #     return(f"{self.name}님의 나이는 {self.age}살 입니다.");
    def __del__(self): # 소멸자
        print(f"{self.name} 객체가 삭제되었습니다.");

stu = Student();
stu.output();
print(stu);
del stu # 객체 삭제