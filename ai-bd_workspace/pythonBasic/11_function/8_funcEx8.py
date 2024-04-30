# 전역변수
# 파이썬 파일 안에서 자유롭게 사용할 수 있는 변수
num = 1;

def func():
    # 함수 안에서 생성하는 변수는 지역변수
    # 지역변수는 함수가 종료되면 사라진다
    num = 100;
    print(num);

def func1():
    # 같은 이름의 변수가 없으면 전역변수 사용
    print(num);

func();
func1();
print(num);