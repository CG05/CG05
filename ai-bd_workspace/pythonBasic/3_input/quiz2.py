w1 = float(input("첫번째 물건 무게 입력 : "));
w2 = float(input("두번째 물건 무게 입력 : "));
lastWeight = 600 - w1 - w2;
print(f"현재 남은 무게 : {lastWeight :.1f} kg");