# 키오스크 - 커피숍
# 제품 출력 - 아메리카노, 카푸치노, 라떼, 에이드, 티
# 아메리카노 - 아이스, 핫
# 카푸치노 - 핫
# 라떼 - 고구마, 바닐라, 슈크림, 말차 - 아이스, 핫
# 에이드 - 레몬, 청포도, 딸기, 복숭아 - 아이스
# 티 - 녹차, 아이스티, 얼그레이, 밀크티 - 아이스, 핫
# 선택 - 선택시 장바구니, 완료되면 결제로
# 결제 - 페이, 카드
import os;

groupDict = {"아메리카노" : [{"":1500},["아이스", "핫"]], "카푸치노" : [{"":2500},["핫"]], "라떼" : [{"고구마": 3200, "바닐라":3000, "슈크림":3800, "말차":3500},["아이스", "핫"]], "에이드" : [{"레몬":3300, "청포도":3300, "딸기":3500, "복숭아":2500},["아이스"]], "티" : [{"녹차":2600, "아이스티":2000, "얼그레이":3800, "밀크티":4000},["아이스", "핫"]]};
payList = ["페이", "카드"];
shopDict = {};
while True:
    selectGroup = "";
    selectShopEdit = "";
    selectHotOrIce = "";
    selectItem = "";
    num = "";
    
    os.system("cls");
    while True:
        os.system("cls");
        print(f"장바구니 : {shopDict}");
        total = 0;
        for name in shopDict:
            total += shopDict.get(name)[0] * shopDict.get(name)[1];
        print(f"현재 장바구니 총 금액 : {total}원")
        groupList = list(groupDict.keys());
        if selectGroup == "":
            for i, group in enumerate(groupDict):
                print(f"{i+1}. {group}",end=" ");
            print();
            selectGroup = input("메뉴 그룹을 선택해주십시오. #:장바구니 결제 0:장바구니 편집 >> ");
            if selectGroup == "#":
                if len(shopDict) == 0:
                    print("아직 장바구니에 상품이 없습니다. 상품을 장바구니에 담아주세요.");
                    selectGroup = "";
                    os.system("pause");
                    continue;
                else:
                    print("현재 장바구니 내의 상품을 결제합니다.");
                    break;
            elif selectGroup == "0":
                print("장바구니를 편집합니다.");
                for i, name in enumerate(shopDict):
                    print(f"{i+1}. {name} x {shopDict.get(name)[1]}잔");
                selectShopEdit = input("편집할 메뉴 번호를 선택해주십시오. #:전체 초기화 0:취소 >> ");
                if selectShopEdit == "0":
                    print("메뉴 선택이 취소되었습니다. 메인으로 돌아갑니다.");
                    selectGroup = "";
                    selectShopEdit = "";
                    os.system("pause");
                    continue;
                elif selectShopEdit == "#":
                    print("장바구니가 전체 초기화됩니다.");
                    shopDict.clear();
                    selectGroup = "";
                    selectShopEdit = "";
                    os.system("pause");
                    continue;
                elif selectShopEdit.isdigit():
                    if 0 < int(selectShopEdit) <= len(shopDict):
                        selectShopEdit = int(selectShopEdit);
                    else:
                        print("잘못된 입력입니다. 다시 입력해주세요.");
                        os.system("pause");
                        continue;
                else:
                    print("잘못된 입력입니다. 다시 입력해주세요.");
                    os.system("pause");
                    continue;
                shopNameList = list(shopDict.keys());
                selectShopName = shopNameList[selectShopEdit-1];
                numBefore = shopDict.get(selectShopName)[1];
                numEdit = input(f"{selectShopEdit}. {selectShopName} 을 몇 잔으로 변경하시겠습니까? 0:메뉴 삭제 >> ");
                if numEdit == "0":
                    print("메뉴를 0잔으로 바꾸어 장바구니에서 삭제됩니다.");
                    shopDict.pop(selectShopName);
                    selectGroup = "";
                    selectShopEdit = "";
                    os.system("pause");
                    continue;
                elif numEdit.isdigit():
                    numEdit = int(numEdit);
                    if numEdit == numBefore:
                        print("이전과 같은 수량 입력으로 편집이 취소됩니다.");
                        selectGroup = "";
                        selectShopEdit = "";
                        os.system("pause");
                        continue;
                    else:
                        print(f"{selectShopEdit}. {selectShopName} 을 {numEdit}잔으로 변경하였습니다.");
                        shopDict[selectShopName][1] = numEdit;
                        selectGroup = "";
                        selectShopEdit = "";
                        os.system("pause");
                        continue;
                else:
                    print("잘못된 입력입니다. 다시 입력해주세요.");
                    os.system("pause");
                    continue;
            elif selectGroup.isdigit():
                if 0 < int(selectGroup) <= len(groupList):
                    selectGroup = int(selectGroup);
                else:
                    print("잘못된 입력입니다. 다시 입력해주세요.");
                    selectGroup = "";
                    os.system("pause");
                    continue;
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.");
                selectGroup = "";
                os.system("pause");
                continue;
        
        selectGroupName = groupList[selectGroup - 1];
        itemDict = groupDict.get(selectGroupName)[0];
        itemNameList = list(itemDict.keys());
        itemChargeList = list(itemDict.values());
        iceHot = list(groupDict.get(selectGroupName)[1]);
        selectItemName = "";
        selectHotOrIce = "";
        selectItemCharge = 0;
        print(f"{selectGroupName}을 선택하셨습니다.");
        if len(itemDict) > 1 and selectItem == "":
            for i, item in enumerate(itemDict):
                print(f"{i+1}. {item}",end=" ");
            print();
            if selectItem == "":
                selectItem = input("상세 메뉴를 선택해주십시오. 0:취소 >> ");
                if selectItem == "0":
                    print("메뉴 선택이 취소되었습니다. 메인으로 돌아갑니다.");
                    selectGroup = "";
                    selectHotOrIce = "";
                    selectItem = "";
                    os.system("pause");
                    continue;
                elif selectItem.isdigit():
                    if 0 < int(selectItem) <= len(itemNameList):
                        selectItem = int(selectItem);
                    else:
                        print("잘못된 입력입니다. 다시 입력해주세요.");
                        selectItem = "";
                        os.system("pause");
                        continue;
                else:
                    print("잘못된 입력입니다. 다시 입력해주세요.");
                    selectItem = "";
                    os.system("pause");
                    continue;
            
            selectItemName = itemNameList[selectItem-1];
            selectItemCharge = itemChargeList[selectItem-1]
        else:
            selectItemName = itemNameList[0];
            selectItemCharge = itemChargeList[0];
        for i, v in enumerate(iceHot):
            print(f"{i+1}. {v}",end=" ");
            print();
        if selectHotOrIce == "":
            selectHotOrIce = input("핫 또는 아이스를 선택해주십시오. 0:취소 >> ");
            if selectHotOrIce == "0":
                print("메뉴 선택이 취소되었습니다. 메인으로 돌아갑니다.");
                selectGroup = "";
                selectHotOrIce = "";
                selectItem = "";
                os.system("pause");
                continue;
            elif selectHotOrIce.isdigit():
                if 0 < int(selectHotOrIce) <= len(iceHot):
                    selectHotOrIce = int(selectHotOrIce);
                else:
                    print("잘못된 입력입니다. 다시 입력해주세요.");
                    selectHotOrIce = "";
                    os.system("pause");
                    continue;
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.");
                selectHotOrIce = "";
                os.system("pause");
                continue;
        
        hotOrIce = iceHot[selectHotOrIce-1];
        fullName = f"{selectItemName} {selectGroupName} ({hotOrIce})";
        if num == "":
            num = input("주문 수량을 선택해주십시오. 0:취소 >> ");
            if num == "0":
                print("수량 선택이 취소되었습니다. 메인으로 돌아갑니다.");
                selectGroup = "";
                num = "";
                selectItem = "";
                selectHotOrIce = "";
                os.system("pause");
                continue;
            elif num.isdigit():
                    num = int(num);
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.");
                num = "";
                os.system("pause");
                continue;
        shopDict[fullName] = [selectItemCharge, num];
        goBreak = input(f"{fullName} {num}잔이 장바구니에 담겼습니다. 바로 결제하시겠습니까? (y)");
        if goBreak == "y" or goBreak == "Y":
            print("결제를 진행합니다.");
            break;
        else:
            print("메인으로 돌아갑니다.");
            selectGroup = "";
            selectHotOrIce = "";
            selectItem = "";
            num = "";

    print(f"= 선택한 메뉴 목록 =");
    total = 0;
    for name in shopDict:
        print(f"{name} x {shopDict.get(name)[1]}잔\t - {shopDict.get(name)[0] * shopDict.get(name)[1]}원");
        total += shopDict.get(name)[0] * shopDict.get(name)[1];
    print(f"총 금액\t - {total}원");
    print("=" * 20);
    for i, pay in enumerate(payList):
        print(f"{i+1}. {pay}", end=" ");
    print();
    while True:
        selectPayment = input("결제 수단을 선택해주십시오. 0:취소 >> ");
        if selectPayment == "0":
            print("결제가 취소되었습니다. 메인으로 돌아갑니다.");
            os.system("pause");
            break;
        elif selectPayment.isdigit():
            if 0 < int(selectPayment) <= len(payList):
                selectPayment = int(selectPayment);
                print(f"선택하신 {payList[selectPayment-1]}(으)로 결제가 진행됩니다.");
                os.system("pause");
                print(f"총 {total}원이 {payList[selectPayment-1]}로 결제가 완료되었습니다.");
                print("감사합니다.");
                shopDict.clear();
                os.system("pause");
                break;
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.");
                continue;
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.");
            continue;



        