saveStr = "Hello Python Fun";
for i in range(3):
    find = input("찾을 문자열 입력 : ");
    if find in saveStr:
        print("찾는 문자열이 포함되어있습니다.");
    else:
        print("찾는 문자열이 포함되어있지 않습니다.");
