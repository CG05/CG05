# 샷건 룰렛
# 2 이상 ~ 8 이하 장전
# 실탄 발수는 1 이상 ~ (장전발수/2) 이하, 나머지는 공포탄
# 공포탄을 자신에게 쏘면 자신 턴 1회 추가
# 실탄을 맞으면 체력 1 감소
# 재장전시 유저부터 시작
# 아이템 :
# 돋보기 - 현재 약실의 탄 확인
# 전화기 - 남아있는 탄 중 무작위 번째의 탄 확인
# 수갑 - 상대 턴 1회 무시
# 화약 - 이번 턴 실탄 발사시 상대 체력 1 추가 감소
# 변환기 - 현재 약실의 탄을 반대로 변경(실탄 -> 공포탄, 공포탄 -> 실탄)
# 아이템 소모이후 4번째 턴이 돌아올 시 아이템 복구 
# 딜러는 현재 탄을 아는 상황이 아니면 돋보기 -> 전화기 순으로 턴당 한 번씩 사용
# 수갑은 사용 가능하면 무조건 사용
# 현재 약실의 탄이 실탄일 확률이 70$ 이상일 경우
# 화약 사용 가능 시 무조건 사용 후 유저 겨냥
# 현재 약실의 탄이 실탄일 확률이 50% 이상일 경우
# 무조건 유저 겨냥
# 현재 약실의 탄이 실탄일 확률이 50% 미만일 경우
# 변환기 사용 가능 시 변환기 무조건 사용 후 유저 겨냥
# 변환기 사용 불가능 시 무조건 본인 겨냥
# 
# 체력 : 4
# 딜러 사망 시 20000원, 룰렛 이어서 진행시 2배씩 증가

from random import randrange, shuffle
import os;
main = True;
money = 0;

def reload():
    global bulletLs, dealerKnows;
    bulletNum = randrange(2, 9);
    realNum = randrange(1, int(bulletNum/2) + 1);

    for i in range(realNum):
        bulletLs.append("real");
        dealerKnows.append("");
    for j in range(bulletNum - realNum):
        bulletLs.append("fake");
        dealerKnows.append("");
    
    shuffle(bulletLs);

def restoreItems():
    global userItem, dealerItem;
    for item in userItem:
        if userItem[item] > 0:
            userItem[item] += 1;
        if userItem[item] == 5:
            userItem[item] = 0;
            print(f"user의 {item}이 복구되었습니다.");
    for item in dealerItem:
        if dealerItem[item] > 0:
            dealerItem[item] += 1;
        if dealerItem[item] == 5:
            dealerItem[item] = 0;
            print(f"dealer의 {item}이 복구되었습니다.");

def phoneCall(bulletLs):
    rand = randrange(0, len(bulletLs));
    print(rand);
    return rand;

def changer():
    global curBullet;
    if curBullet == "fake":
        curBullet == "real";
    elif curBullet == "real":
        curBullet == "fake";

while main:
    os.system("cls");
    userItem = {"돋보기" : 0, "전화기" : 0, "수갑" : 0, "화약" : 0, "변환기" : 0};
    dealerItem = {"돋보기" : 0, "전화기" : 0, "수갑" : 0, "화약" : 0, "변환기" : 0};
    userHp = 4;
    dealerHp = 4;
    userTurn = 1;
    damage = 1;
    bulletLs = [];
    dealerKnows = []
    curBullet = "";
    print("###### 샷건 룰렛 게임 ######");
    while userHp > 0 and dealerHp > 0:
        os.system("pause");
        os.system("cls");
        if len(bulletLs) == 0:
            print("새로운 라운드가 시작되어 재장전합니다.");
            reload();
            print(f"이번 라운드는 {len(bulletLs)}발 (실탄: {bulletLs.count("real")}, 공포탄: {bulletLs.count("fake")}) 로 진행됩니다.");
            userTurn = 1;
        restoreItems();
        curBullet = bulletLs[0];
        damage = 1;
        if userTurn <= 0:
            print("딜러의 턴이 진행됩니다.");
            if dealerItem["돋보기"] == 0 and dealerKnows[0] == "":
                print("딜러가 돋보기를 사용합니다.");
                dealerKnows[0] = curBullet;
                dealerItem["돋보기"] = 1;
            elif dealerItem["전화기"] == 0 and dealerKnows[0] == "":
                print("딜러가 전화기를 사용합니다.");
                getRandBullet = phoneCall(bulletLs);
                dealerKnows[getRandBullet] = bulletLs[getRandBullet];
                dealerItem["전화기"] = 1;
            if dealerItem["수갑"] == 0:
                print("딜러가 수갑을 사용합니다.");
                dealerItem["수갑"] = 1;
                userTurn = -1;
            realOption = 0;
            if dealerKnows[0] == "real":
                realOption = 1;
            elif dealerKnows[0] == "fake":
                realOption = 0;
            else:
                leftReal = bulletLs.count("real");
                realOption = leftReal / len(bulletLs);
            toUser = True;
            if realOption >= 0.7:
                if dealerItem["화약"] == 0:
                    print("딜러가 화약을 사용합니다.");
                    dealerItem["화약"] = 1;
                    damage = 2;
                toUser = True;
            elif realOption >= 0.5:
                toUser = True;
            else:
                if dealerItem["변환기"] == 0:
                    print("딜러가 변환기를 사용합니다.");
                    dealerItem["변환기"] = 1;
                    changer();
                    toUser = True;
                    
                else:
                    toUser = False;
            if toUser:
                print("딜러가 유저를 향해 방아쇠를 당깁니다!");
                userTurn += 1;
                if curBullet == "real":
                    print("실탄이 발사됩니다!!");
                    userHp -= damage;
                    print(f"유저가 {damage}의 피해를 입어 체력이 {userHp} 남았습니다.");
                elif curBullet == "fake":
                    print("공포탄이 발사됩니다. 유저는 피해를 입지 않았습니다.");
            else:
                print("딜러가 자신을 향해 방아쇠를 당깁니다.");
                if curBullet == "real":
                    print("실탄이 발사됩니다!!");
                    dealerHp -= damage;
                    print(f"딜러가 {damage}의 피해를 입어 체력이 {dealerHp} 남았습니다.");
                    userTurn += 1;
                elif curBullet == "fake":
                    print("공포탄이 발사됩니다. 딜러는 피해를 입지 않았습니다.");
        
        elif userTurn > 0:
            print("유저의 턴이 진행됩니다.");
            toDealer = None;
            while toDealer == None:
                selectMenu = input("1.딜러에게 겨냥 2.자신에게 겨냥 3.아이템사용 >> ");
                if selectMenu == "1":
                    toDealer = True;
                    break;
                elif selectMenu == "2":
                    toDealer = False;
                    break;
                elif selectMenu == "3":
                    itemLs = list(userItem.keys());
                    use = None
                    while use == None:
                        for i, item in enumerate(userItem):
                            if userItem[item] == 0:
                                print(f"{i+1}.{item}");
                        selectItem = input("사용할 아이템을 선택 0.취소 >>");
                        if selectItem == "0":
                            print("아이템 사용을 취소합니다.");
                            break;
                        else:
                            if selectItem.isdigit():
                                use = itemLs[int(selectItem)-1];
                                print(f"유저가 {use}를 사용합니다.");
                                userItem[use] = 1;
                    if use != None:
                        # "돋보기" : 0, "전화기" : 0, "수갑" : 0, "화약" : 0, "변환기" : 0
                        if use == "돋보기":
                            print(f"현재 약실에 있는 탄은 {curBullet}입니다.");
                        elif use == "전화기":
                            getRandBullet = phoneCall(bulletLs);
                            print(f"{getRandBullet+1}번째에 있는 탄은 {bulletLs[getRandBullet]}입니다.");
                        elif use == "수갑":
                            print("딜러에게 수갑을 채워 이번 턴과 관계없이 다음 턴은 유저에게 이어집니다.");
                            userTurn -= 1;
                        elif use == "화약":
                            print("화약을 사용하여 이번 턴 실탄의 데미지를 1 증가시킵니다.");
                            damage = 2;
                        elif use == "변환기":
                            print("변환기를 사용하여 현재 약실의 탄을 반대로 변경합니다.");
                            changer();
                        os.system("pause");
                    else:
                        continue;
            
            if toDealer:
                print("유저가 딜러를 향해 방아쇠를 당깁니다!");
                userTurn -= 1;
                if curBullet == "real":
                    print("실탄이 발사됩니다!!");
                    dealerHp -= damage;
                    print(f"딜러가 {damage}의 피해를 입어 체력이 {dealerHp} 남았습니다.");
                elif curBullet == "fake":
                    print("공포탄이 발사됩니다. 딜러는 피해를 입지 않았습니다.");
            else:
                print("유저가 자신을 향해 방아쇠를 당깁니다.");
                if curBullet == "real":
                    print("실탄이 발사됩니다!!");
                    userHp -= damage;
                    print(f"유저가 {damage}의 피해를 입어 체력이 {userHp} 남았습니다.");
                    userTurn -= 1;
                elif curBullet == "fake":
                    print("공포탄이 발사됩니다. 유저는 피해를 입지 않았습니다.");

        bulletLs.pop(0);
        dealerKnows.pop(0);
    if userHp == 0:
        print("패배하셨습니다...");
        os.system("pause");
    if dealerHp == 0:
        print("승리하셨습니다!!!");
        if money == 0:
            money = 20000;
        else:
            money *= 2;
        continueGame = input(f"보유 금액이 {money}원이 되었습니다. 묻고 더블로 가시겠습니까?(y)");
        if continueGame == "y" or continueGame == "Y":
            print("묻고 더블로 가!!");
            os.system("pause");
        else:
            print("게임을 종료합니다.");
            main = False;

                    


