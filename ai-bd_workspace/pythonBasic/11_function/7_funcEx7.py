# 함수의 반환데이터는 1개만 가능하다.
# 파이썬에서는 tuple로 packing 해서 반환 -> unpacking으로 여러 값을 받을 수 있다.
def func():
    num1 = int(input("첫 번째 정수 입력 : "));
    num2 = int(input("두 번째 정수 입력 : "));
    print(f"{num1}, {num2}");
    return num1, num2;

num1, num2 = func();
print(f"{num1}, {num2}");

def func1():
    ls = [1,2,3];
    dict = {1:"1", 2:"2"};
    return ls, dict;

ls, dict = func1();
print(f"{ls}, {dict}");