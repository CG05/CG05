def func(num, *nums):
    print(f"{num}, {nums}");
# *매개변수 : 가변인자 - 여러 개의 값을 tuple로 받아 처리하므로 받아야 할 매개변수의 개수가 달라질 때 사용
func(1,2,3,4,5);

def func1(*nums):
    print(f"{nums}");
func1(1,2,3,4,5);