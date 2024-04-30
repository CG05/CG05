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
# 아이템 소모이후 2번 장전할 시 아이템 복구 
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
main = True;
money = 0;
menu = ("")

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
    
    bulletLs.shuffle();

def restoreItems():
    global userItem, dealerItem;
    for item in userItem:
        if userItem[item] > 0:
            userItem[item] += 1;
        if userItem[item] == 3:
            userItem[item] = 0;
            print(f"user의 {item}이 복구되었습니다.");
    for item in dealerItem:
        if dealerItem[item] > 0:
            dealerItem[item] += 1;
        if dealerItem[item] == 2:
            dealerItem[item] = 0;
            print(f"dealer의 {item}이 복구되었습니다.");

while main:
    userItem = {"돋보기" : 0, "전화기" : 0, "수갑" : 0, "화약" : 0, "변환기" : 0};
    dealerItem = {"돋보기" : 0, "전화기" : 0, "수갑" : 0, "화약" : 0, "변환기" : 0};
    userHp = 4;
    dealerHp = 4;
    userTurn = 1;
    damage = 1;
    bulletLs = [];
    dealerKnows = []
    curBullet = "";
    while userHp > 0 and dealerHp > 0:
        if len(bulletLs) == 0:
            print("라운드가 종료되어 재장전합니다.");
            reload();
            print(f"이번 라운드는 {len(bulletLs)}발 (실탄: {bulletLs.count("real")}, 공포탄: {bulletLs.count("fake")}) 로 진행됩니다.");
            userTurn = 1;
        restoreItems();
        curBullet = bulletLs[0];
        if userTurn == 0:
            print("딜러의 턴이 진행됩니다.");
            if dealerItem["돋보기"] == 0 and dealerKnows[0] == "":
                print("딜러가 돋보기를 사용합니다.");
                dealerKnows[0] = curBullet;
                dealerItem["돋보기"] = 1;
            elif dealerItem["전화기"] == 0 and dealerKnows[0] == "":
                print("딜러가 전화기를 사용합니다.");
                getRandBullet = randrange(0, len(bulletLs)+1)
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
                    damage = 2;
                toUser = True;
            elif realOption >= 0.5:
                toUser = True;
            else:
                if dealerItem["변환기"] == 0:
                    print("딜러가 변환기를 사용합니다.");
                    


