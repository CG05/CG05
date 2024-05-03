class Parent:
    def aaa(self):
        print("부모 aaa메서드");

class Child(Parent):
    # override : 부모 클래스의 함수를 자식 클래스가 변경
    def aaa(self): # override
        print("자식 aaa메서드");


p = Parent();
c = Child();

p.aaa();
c.aaa();