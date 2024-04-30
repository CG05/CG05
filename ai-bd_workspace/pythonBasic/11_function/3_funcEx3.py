def func(num1 = 20, num2 = 100):
    print(f"{num1}, {num2}");

func(10);
# 기본값이 설정되어있는 매개변수는 값을 넘기지 않으면 기본값으로 작동
func();

# def func1(num1 = 20, num2):
#     print(f"{num1}, {num2}");
# 첫 번째 매개변수를 생략하고 두 번째 매개변수만 넣을 수 없다 -> 기본값이 있는 매개변수는 뒤로
def func1(num2, num1 = 20):
    print(f"{num1}, {num2}");