# 함수는 기본적으로 4가지 형태
# 매개변수 : 함수를 호출할 때 데이터를 넘겨받는 변수
# 1. 매개변수 x 반환데이터 x ex)출력용 함수
def output():
    print("#### 계산기 ####");
output();

# 2. 매개변수 x 반환데이터 o
def inputNum():
    num = int(input("정수 입력 : "));
    # return : 데이터를 반환하거나 함수를 종료할 때 사용
    return num;
num1 = inputNum();
num2 = inputNum();

# 3. 매개변수 o 반환데이터 x
def result(a, b):
    print(f"{a} + {b} = {a + b}");
result(num1, num2);

# 4. 매개변수 o 반환데이터 o
def different(num1):
    num1 += 1000;
    print(num1);
    return num1;
num3 = different(num1);
print(num1);
print(num3);