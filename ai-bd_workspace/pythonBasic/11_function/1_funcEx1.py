# 함수는 def로 시작
# def [함수명] (매개변수):
#     내용;
def add():
    num1 = int(input("첫 번째 정수 입력 : "));
    num2 = int(input("두 번째 정수 입력 : "));

    print(f"{num1} + {num2} = {num1 + num2}");

# 함수는 호출해야만 사용 가능
# [함수명] (매개변수);
add();