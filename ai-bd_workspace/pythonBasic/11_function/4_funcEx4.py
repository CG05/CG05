def func(num1, num2):
    print(f"{num1}, {num2}");
func(5, 10);
# 매개변수명을 직접 지정하여 대입할 수 있다
func(num2=5, num1=10);
num1 = 5;
num2 = 10;
func(num2=num1,num1=num2);
