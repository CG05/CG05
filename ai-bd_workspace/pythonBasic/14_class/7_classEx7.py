class Parent: # 이름과 나이를 가진 클래스 
    name = "홍길동";
    age = 20;
    def aaa(self):
        print(f"{self.name}, {self.age} 가진 클래스 메서드");

class Child(Parent): # 이름, 나이, 이메일, 주소 -> 상속을 통해 Parent와 변수와 함수를 같이 가질 수 있음
    # name = "홍길동"
    # age = 20;
    email = "hong@test.com";
    address = "서울 동작구";
    def bbb(self):
        print(f"{self.name}, {self.age}, {self.email}, {self.address} 가진 클래스 메서드");

# 파이썬은 다중상속을 지원한다.

p = Parent();
p.aaa();

c = Child();
c.aaa();
c.bbb();