# 사칙연산 프로그램
# 2개의 정수 입력
# +,-,*,/ 선택
# 결과값 출력
def calc(select, a, b):
    if select == 1:
        return a + b;
    elif select == 2:
        return a - b;
    elif select == 3:
        return a * b;
    elif select == 4 and b != 0:
        return a / b;
    else:
        print("잘못된 입력입니다.");
        return None;

def inputCorrect(iStr):
    if not iStr.isdigit():
        print("잘못된 입력입니다.");
        return False;
    else:
        return True;

def getNum():
    num = input(">> ");
    if inputCorrect(num):
        return int(num);
    else:
        return None;

def inputNum(prtStr):
    print(prtStr);
    return getNum();
    
def isNone(num):
    if num == None:
        return True;
    else:
        return False;

while True:
    num1 = inputNum("첫 번째 정수를 입력하세요");
    if isNone(num1): continue;

    num2 = inputNum("두 번째 정수를 입력하세요");
    if isNone(num2): continue;

    calcSelect = inputNum("1.+ 2.- 3.* 4./ 사칙연산중 선택하세요");
    if isNone(calcSelect): continue;

    result = calc(calcSelect, num1, num2);

    if isNone(result): continue;
    else:
        print(f"결과값은 {result}입니다.");
    