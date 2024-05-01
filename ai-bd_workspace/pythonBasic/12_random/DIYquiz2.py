# up down 게임
# 1~100 안의 수 무작위 선택

from random import randrange
import os;

main = True;
while main:
    os.system("cls");
    print("Up Down 게임입니다.");
    os.system("pause");
    count = 5;
    notFound = True
    num = randrange(1, 101);
    while count > 0 and notFound:
        user = int(input("예상 숫자를 입력 : "));
        if user == num:
            print("정답입니다!");
            notFound = False;
        elif user < num:
            print("Up입니다.");
            count -= 1;
        else:
            print("Down입니다.");
            count -= 1;
    if notFound:
        print("제한 횟수 초과로 패배입니다.");
    else:
        print("승리입니다.")
    os.system("pause");
