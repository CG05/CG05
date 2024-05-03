class Parent1:
    

    def __init__(self) -> None:
        self.school = "KG고";
        self.grade = "3학년";
        self.group = "1반";
        print("Parent1 init함수");
    
    def __str__(self) -> str:
        return f"{self.school}, {self.grade}, {self.group}";

# override시 변경할 내용만 변경이 가능하다
class Child1(Parent1):
    def __init__(self) -> None:
        super().__init__();
        self.group = "2반";

class Child2(Parent1):
    def __init__(self) -> None:
        super().__init__();
        self.grade = "2학년";
        self.group = "3반";
    


p1 = Parent1();
print(p1)
c1 = Child1();
print(c1);
c2 = Child2();
print(c2);