# 베스킨라빈스 게임
# 30 26 22 18 14 10 6 2 : 필승숫자 -> 이 숫자들을 자신의 턴마다 말하고 끝내면 무조건 이김
print("<베스킨라빈스 게임>");
print("!그만 말하고 싶다면 0을 입력하세요!");

first = -1;
user, com = 0, 0;
userLast, comLast = 0, 0;
next = 1;
cycle = 0;

while first != 1 and first != 0:
    first = int(input("선공을 원하시면 0, 후공을 원하시면 1을 입력하세요 : "));
if first == 0:
    print("게임 시작! 당신이 선공입니다. 1부터 입력하세요.");
    i = 0;
    while i < 3:
        userIn = int(input(f"남은 기회 : {3 - i} - 숫자를 입력하세요 : "));
        if userIn == next:
            userLast = userIn;
            next = userLast + 1;
            i += 1;
        elif userIn == 0 and i > 0:
            break;
        else:
            print("잘못된 입력입니다. 다시 입력하세요.");

else:
    print("게임 시작! 당신이 후공입니다.");


if userLast >= 2 :
    cycle = 1;

while(userLast < 31):
    if userLast == 30:
        print("당신의 승리입니다.");
        break;
    
    if 0 < cycle * 4 + 2 - userLast <= 3:
        for i in range(cycle * 4 + 2 - userLast):
            print(f"com : {userLast + i + 1}");
        comLast = cycle * 4 + 2;
    else:
        print(f"com : {userLast + 1}");
        comLast = userLast + 1;
    
    j = 0;
    next = comLast + 1;
    while j < 3:
        userIn = int(input(f"남은 기회 : {3 - j} - 숫자를 입력하세요 : "));
        
        if userIn == next:
            userLast = userIn;
            next = userLast + 1;
            if userIn == 31:
                print("컴퓨터의 승리입니다.");
                break;
            else:                                                                                                                              
                j += 1;
        elif userIn == 0 and i > 0:
            break;
            
        else:
            print("잘못된 입력입니다. 다시 입력하세요.");
    
    if 0 < (cycle + 1) * 4 + 2 - userLast <= 3:
        cycle += 1;

