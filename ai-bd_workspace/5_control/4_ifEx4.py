num = int(input("정수 입력 : "));
if num > 0:
    if num%2 == 0:
        print(f"{num}은 짝수입니다.");
    else:
        print(f"{num}은 홀수입니다.");
else:
    print(f"{num}은 0 또는 음수입니다.");
