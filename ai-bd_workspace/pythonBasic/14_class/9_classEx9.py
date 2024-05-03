class Parent:
    def __init__(self) -> None:
        self.name = input("이름 입력 : ");

    def __str__(self) -> str:
        return f"{self.name} 님"

class Child(Parent):
    # super() : 부모 클래스
    def __init__(self) -> None:
        super().__init__();
        self.age = input("나이 입력 : ");

    def __str__(self) -> str:
        msg = super().__str__();
        msg += f"\n{self.age}세\n반갑습니다."
        return msg;
    

p = Parent();
print(p);
c = Child();
print(c);