main = True;
money = 0;
cofMax = 50;
cocMax = 50;
cupMax = 150;
coffee = 10;
cocoa = 10;
cup = 10;
cofStat = "[O]";
cocStat = "[O]";
cofAccount = 0;
cocAccount = 0;

while main :
    if money == 0 and cup > 0:
        money = int(input("환영합니다. 자판기에 요금을 투입해주세요 : "));
    elif money == 0 and cup == 0:
        code = int(input("컵 부족으로 판매할 수 없습니다. 관리자는 코드를 입력해주십시오 : "));
        if code == -1:
            money = code;
        else:
            continue;
    elif cup == 0:
        print(f"컵 부족으로 판매할 수 없습니다. 잔액 {money}가 반환됩니다.");
        money = 0;
        continue;
    if coffee == 0:
        cofStat = "[X]";
    else:
        cofStat = "[O]";
    if cocoa == 0:
        cocStat = "[X]";
    else:
        cocStat = "[O]";
    if money == -1:
        while True:
            print("# >> 관리자 메뉴 <<");
            print("# [1] 커피 잔량 [2] 코코아 잔량 [3] 컵 잔량 [4] 판매현황 조회 [9] 나가기 [0] 자판기 종료");
            select = input("# 메뉴에서 선택해주세요 >> ");
            
            if select == "1":
                print(f"# 커피 잔량은 {coffee}잔 입니다.", end=" ");
                if coffee == cofMax:
                    print("[FULL]");
                cofCharge = int(input("추가하시겠습니까? >> "))
                if cofCharge > 0:
                    if coffee + cofCharge > cofMax:
                        coffee = cofMax;
                        print(f"# 최대치로 추가되어 현재 잔량은 {coffee}잔 입니다.");
                    else:
                        coffee += cofCharge;
                        print(f"# {cofCharge}잔이 추가되어 현재 잔량은 {coffee}잔 입니다.");
                elif cofCharge == 0:
                    print("# 잔량이 추가되지 않았습니다.");
            elif select == "2":
                print(f"# 코코아 잔량은 {cocoa}잔 입니다.", end=" ");
                if cocoa == cocMax:
                    print("[FULL]");
                cocCharge = int(input("추가하시겠습니까? >> "))
                if cocCharge > 0:
                    if cocoa + cocCharge > cocMax:
                        cocoa = cocMax;
                        print(f"# 최대치로 추가되어 현재 잔량은 {cocoa}잔 입니다.");
                    else:
                        cocoa += cocCharge;
                        print(f"# {cocCharge}잔이 추가되어 현재 잔량은 {cocoa}잔 입니다.");
                elif cocCharge == 0:
                    print("# 잔량이 추가되지 않았습니다.");
            elif select == "3":
                print(f"# 컵 잔량은 {cup}잔 입니다.", end=" ");
                if cup == cupMax:
                    print("[FULL]");
                cupCharge = int(input("추가하시겠습니까? >> "))
                if cupCharge > 0:
                    if cup + cupCharge > cupMax:
                        cup = cupMax;
                        print(f"# 최대치로 추가되어 현재 잔량은 {cup}잔 입니다.");
                    else:    
                        cup += cupCharge;
                        print(f"# {cupCharge}잔이 추가되어 현재 잔량은 {cup}잔 입니다.");
                elif cupCharge == 0:
                    print("# 잔량이 추가되지 않았습니다.");
            elif select == "4":
                print(f"#\t ||  커피\t판매량 :  {cofAccount:>3d}잔  ||  커피\t판매수익 :  {cofAccount * 200:>5d}원  ||");
                print(f"#\t ||  코코아\t판매량 :  {cocAccount:>3d}잔  ||  코코아\t판매수익 :  {cocAccount * 250:>5d}원  ||");
                print(f"#\t ||  전체\t판매량 :  {cofAccount + cocAccount:>3d}잔  ||  전체\t판매수익 :  {cofAccount * 200 + cocAccount * 250:>5d}원  ||");
            elif select == "9":
                print("# 관리자 메뉴를 나갑니다.");
                money = 0;
                break;
            elif select == "0":
                print("# 자판기를 종료합니다.");
                main = False;
                break;
            else:
                print("# 입력이 잘못되었습니다. 메뉴 내에서 선택해주십시오.");
        continue;

    
    print("=========================== 메 뉴 ===========================", end="\n  ");
    if money >= 200:
        print(f"1: 커피(200){cofStat}", end= " ");
    else:
        print(f"1: 커피(200){cofStat}", end= " ");
    if money >= 250:
        print(f"2: 코코아(250){cocStat}", end= " ");
    else:
        print(f"2: 코코아(250){cocStat}", end= " ");
    print("3: 반환 4: 추가요금투입");
    print(f"-< 잔액 : {money}원 >-")
    select = input("메뉴에서 선택해주세요 : ");
    if select == "1":
        if money >= 200 and cofStat == "[O]":
            money -= 200;
            coffee -= 1;
            cup -= 1;
            cofAccount += 1;
            print("커피(200)을 선택하셨습니다.");
        else:
            print("구매할 수 없습니다.");
    elif select == "2":
        if money >= 250 and cocStat == "[O]":
            money -= 250;
            cocoa -= 1;
            cup -= 1;
            cocAccount += 1;
            print("코코아(250)을 선택하셨습니다.");
        else:
            print("구매할 수 없습니다.");
    elif select == "3":
        print(f"반환을 선택하셨습니다. {money}원이 반환됩니다.");
        money = 0;
    elif select == "4":
        money += int(input("추가할 요금을 투입해주세요 : "));
    else:
        print("입력이 잘못되었습니다. 메뉴 내에서 선택해주십시오.");
