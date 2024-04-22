# id() : 변수의 값의 위치를 출력하는 함수
# 모든 파이썬의 변수의 값은 참조형으로 처리
num1 = 100;
print(id(num1));
num2 = 100;
print(id(num2));
num2 = 200;
print(id(num2));