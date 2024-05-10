import os;
from datetime import datetime

def screenCls():
    os.system("pause");
    os.system("cls");

def getProId(proName):
    with open(dirPath+proName, 'r', encoding="utf-8") as f:
        product = f.readlines();
        if len(product) == 0:
            return 1;
        else:
            proId = product[-1].split(",")[0];
            return int(proId)+1;

def getProduct(proName):
    with open(dirPath+proName, 'r', encoding="utf-8") as f:
        return f.readlines();

def findProductName(sub):
    for i, p in enumerate(productName):
        print(f"{i+1}. {p}");
    subSelect = input(f"{sub}할 품목 번호 입력 : ");

    if subSelect.isdigit():
        return int(subSelect)-1;
    else:
        print("품목 번호는 숫자만 가능합니다.");    
        return -100;


dirPath = "ai-bd_workspace\\product\\";
productName = os.listdir(dirPath);
today = datetime.today().strftime("%Y-%m-%d");

while True:
    print(f"오늘날짜 : {today}");
    print("##### 편의점 재고 관리 #####");
    print("1. 입고");
    print("2. 출고");
    print("3. 제품 수정")
    print("4. 전체 재고 확인");
    print("5. 품목 등록");
    print("6. 품목 삭제");
    print("0. 종료");
    select = input("선택 : ");

    screenCls();

    if select == "1":
        print("### 입고 ###");
        subSelect = findProductName("입고");

        if subSelect != -100:
            if 0 <= int(subSelect) <= len(productName)-1:
                print(f"== {productName[subSelect]} 입고 ==");
                proNo = input("제품등록번호 입력 : ");
                proName = input("제품 이름 입력 : ");
                price = input("가격 입력 : ");
                amount = input("수량 입력 : ");
                proId = getProId(productName[subSelect]);

                with open(dirPath+productName[subSelect], 'a', encoding="utf-8") as f:
                    f.write(f"{proId},{today},{proNo},{proName},{price},{amount}\n");
            else:
                print("없는 품목 번호 입니다.");
    elif select == "2":
        print("### 출고 ###");
        subSelect = findProductName("출고");

        if subSelect != -100:
            if 0 <= int(subSelect) <= len(productName)-1:
                product = getProduct(productName[subSelect])             
                for p in product:
                    p = p.split(",");
                    print(f"{p[0]}. {p[3]}");
                try:
                    no = int(input("출고할 제품 번호 입력 : "));
                    chproduct = '';
                    for i,p in enumerate(product):
                        if i == no-1:
                            p = p.split(",");
                            print(f"현재 수량 : {int(p[5])} 개");
                            amount = input("출고할 수량 입력 : ");
                            if int(amount) <= int(p[5]):
                                amount = int(p[5]) - int(amount);
                                chproduct += f"{p[0]},{p[1]},{p[2]},{p[3]},{p[4]},{amount}\n"
                            else:
                                print("수량을 초과 할 수 없습니다.");
                        else :
                            chproduct += p;
                    with open(dirPath+productName[subSelect], 'w', encoding="utf-8") as f:
                        f.write(chproduct);
                except:
                    print("제품 번호 및 수량은 숫자만 입력 가능합니다.")

            else:
                print("없는 품목 번호 입니다.");
    elif select == "3":
        print("### 제품 수정 ###")
        subSelect = findProductName("제품 수정")

        if subSelect != -100:
            if 0 <= int(subSelect) <= len(productName)-1:
                product = getProduct(productName[subSelect])
                
                for p in product:
                    p = p.split(",");
                    print(f"{p[0]}. {p[3]}");
                try:
                    no = int(input("수정할 제품 번호 입력 : "));
                    chproduct = '';
                    for i,p in enumerate(product):
                        if i == no-1:
                            p = p.split(",");
                            price = input("수정할 가격 입력 : ");
                            amount = input("수정할 수량 입력 : ");
                            chproduct += f"{p[0]},{p[1]},{p[2]},{p[3]},{price},{amount}\n"
                        else :
                            chproduct += p;
                    with open(dirPath+productName[subSelect], 'w', encoding="utf-8") as f:
                        f.write(chproduct);
                except:
                    print("제품 번호 및 수량은 숫자만 입력 가능합니다.")

            else:
                print("없는 품목 번호 입니다.");
    elif select == "4":
        print("### 전체 재고 현황 ###");
        for i in productName:
            product = getProduct(i);
            print(f"=== {i} ===");
            if len(product) != 0:
                for i,p in enumerate(product):    
                    p = p.split(",");
                    print(f"제품명 : {p[3]}");
                    print(f"가격 : {p[4]}");
                    print(f"재고 : {int(p[5])}");
            else:
                print("제품이 없습니다.");
    elif select == "5":
        print("### 품목 등록 ###");
        proName = input("등록할 품목 이름 입력 : ");

        for i in productName:
            if proName == i:
                print(f"{i} 와 같은 품목이 존재합니다.");
                break;
        else:
            open(dirPath + proName, 'w+', encoding="utf-8");
            productName.append(proName);
            print(f"{proName} 품목을 등록했습니다.");
    elif select == "6":
        print("### 품목 삭제 ###");
        subSelect = findProductName("품목 삭제");

        if subSelect != -100:
            if 0 <= subSelect <= len(productName) -1:
                print(f"{subSelect} 품목을 삭제합니다.");
                os.remove(dirPath+productName[subSelect]);
            else:
                print("없는 품목 번호 입니다.");
    elif select == "0":
        print("프로그램을 종료 합니다.");
        break;
    else:
        print("선택된 메뉴 번호가 없습니다.");

    screenCls();
