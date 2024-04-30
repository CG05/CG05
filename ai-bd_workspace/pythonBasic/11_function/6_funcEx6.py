def func(num, **nums):
    print(f"{num}, {nums}");
# **매개변수 : 가변인자(딕셔너리형) - key=value 형태를 받아 딕셔너리 형태로 처리
func(10, k1=20, k2=30);