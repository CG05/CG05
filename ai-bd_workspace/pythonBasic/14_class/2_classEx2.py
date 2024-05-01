# 명명규칙 : 클래스 이름 첫 글자는 대문자, 이어지는 단어에 첫 글자도 대문자
# 명명규칙은 절대적인 것은 아니지만 관례가 그렇다
class Student():
    # 데이터
    name = '';
    kor = 0;
    eng = 0;
    math = 0;
    sum = 0;
    avg = 0;

    # 기능
    # 클래스 함수의 제일 첫 매개변수는 self로 해야 한다.
    def scoreOper(self,name, kor, eng, math):
        self.name = name;
        self.kor = kor;
        self.eng = eng;
        self.math = math;
        self.sum = self.kor + self.eng + self.math;
        self.avg = self.sum / 3;

    def scoreOutput(self):
        print(f"{self.name}님 의 총점은 {self.sum}, 평균은 {self.avg}입니다.");

# 인스턴스 생성
stu1Class = Student();
stu2Class = Student();

stu1Class.scoreOper("홍길동", 100, 90, 80);
stu2Class.scoreOper("이순신", 90, 90, 80);

stu1Class.scoreOutput();
stu2Class.scoreOutput();

print(stu1Class.name);
print(stu2Class.name);