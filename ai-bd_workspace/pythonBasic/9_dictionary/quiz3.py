# 네비게이션
# 등록, 목적지 수정, 검색, 종료
menu = "목적지 목록", "목적지 등록", "목적지로 탐색", "주소로 탐색", "탐색 중단", "종료";
nav = {};
curNavName = "";
curNavAddr = "";
main = True;
print("< KG네비게이션이 시작되었습니다 >")
while main:
    if curNavAddr != "":
        print(f"<<< ~현재 탐색중~ ",end="");
        if curNavName != "":
            print(f" [ {curNavName} ] : ",end="");
        print(f"[ {curNavAddr} ] >>>");
    for i, m in enumerate(menu):
        print(f"{i+1}. {m}",end=" ");
    print();
    select = input("메뉴에서 선택해주십시오 : ");
    if select.isdigit():
        if select == "1":
            editing = False;
            while True:
                if len(nav) == 0:
                    print("###################################################");
                    print("### 목록이 비어있습니다. 목적지를 등록해주세요. ###");
                    print("###################################################");

                    break;
                
                if editing == False:
                    print("================ 목록 ================");
                    for i, name in enumerate(nav):
                        print(f"<{i+1}> [ {name} ]\t: [ {nav.get(name)} ]");
                    print("="*38);
                    print("편집하시려면 해당 목적지의 번호를 입력하세요. 메뉴로 나가시려면 0을 입력하세요.");
                    editSelect = input(">> ");
                if editSelect == "0":
                    print("메뉴로 나갑니다.")
                    break;
                elif 0 < int(editSelect) <= len(nav) :
                    editSelect = int(editSelect);
                    nameList = list(nav.keys());
                    addrList = list(nav.values());
                    if curNavAddr == addrList[editSelect - 1]:
                        print("현재 탐색중인 목적지입니다. 탐색을 중단하고 다시 시도해주세요.");
                        print("메뉴로 나갑니다.");
                        break;
                    print("목적지 이름을 편집하려면 1을, 주소를 편집하려면 2를 입력하세요. 취소하시려면 #를, 삭제하시려면 0을 입력하세요 :");
                    nameOrAddr = input(">> ")
                    if nameOrAddr == "#":
                        print("취소되었습니다. 목록으로 나갑니다.");
                    elif nameOrAddr == "0":
                        print(f"목적지 [ {nameList[editSelect - 1]} ]가 삭제되었습니다.");
                        del nav[nameList[editSelect - 1]];
                        print("목록으로 나갑니다.");
                    elif nameOrAddr == "1":
                        editName = input("새로운 목적지 이름을 입력하세요. 취소하시려면 #를 입력하세요 : ");
                        if editName == "#":
                            print("취소되었습니다. 목록으로 나갑니다.");
                        else:
                            print(f"주소지 [ {nav.get(nameList[editSelect - 1])} ]의 이름이 [ {editName} ]으로 수정되었습니다.");
                            nav[editName] = nav.get(nameList[editSelect - 1]);
                            del nav[nameList[editSelect - 1]];
                            print("목록으로 나갑니다.");
                    elif nameOrAddr == "2":
                        editAddr = input("새로운 목적지 주소를 입력하세요. 취소하시려면 #를 입력하세요 : ");
                        if editAddr == "#":
                            print("취소되었습니다. 목록으로 나갑니다.");
                        else:
                            print(f"목적지 [ {nameList[editSelect - 1]} ]의 주소가 [ {editAddr} ]으로 수정되었습니다.");
                            nav[nameList[editSelect - 1]] = editAddr;
                            print("목록으로 나갑니다.");
                    else:
                        print("잘못 입력하셨습니다. 목록으로 돌아갑니다.");
                    editing = False;
                else:
                    print("잘못 입력하셨습니다. 다시 입력해주세요.");
                    editing = True;
        elif select == "2":
            addr = input("등록할 목적지 주소를 입력해주세요 : ");
            addrList = list(nav.values());
            if addr in addrList:
                print("이미 저장된 주소입니다.")
            else:
                name = input("저장할 이름을 입력해주세요 : ");
                print(f"목적지 [ {name} ] : [ {addr} ]가 저장되었습니다.");
                nav[name] = addr;
        elif select == "3":
            rName = input("탐색할 목적지를 입력해주세요 : ");
            if rName in nav:
                print(f"목적지 [ {rName} ] : [ {nav.get(rName)} ]로 가는 경로를 탐색합니다");
                curNavName = rName;
                curNavAddr = nav.get(rName);
            else:
                print("해당하는 목적지가 없습니다. 등록하거나 주소로 탐색해주세요.");
        elif select == "4":
            rAddr = input("탐색할 주소를 입력해주세요 : ");
            nameList = list(nav.keys());
            addrList = list(nav.values());
            
            for i, addr in enumerate(addrList):
                if addr == rAddr:
                    print(f"목적지 [ {nameList[i]} ] : [ {nav.get(nameList[i])} ]로 가는 경로를 탐색합니다");
                    curNavName = nameList[i];
                    curNavAddr = rAddr;
                    break;
            else:
                print(f"주소 [ {rAddr} ]로 가는 경로를 탐색합니다");
                curNavAddr = rAddr;
                name = input("목적지를 새로 등록할까요? 등록하려면 저장할 이름을, 아니라면 0을 입력하세요 : ");
                if name == "0":
                    print("목적지 등록을 취소했습니다.");
                else:
                    print(f"목적지 [ {name} ] : [ {rAddr} ]가 저장되었습니다.");
                    nav[name] = rAddr;
                    curNavName = name;
        elif select == "5":
            print("탐색을 중단합니다.");
            curNavName = "";
            curNavAddr = "";
        elif select == "6":
            print("네비게이션을 종료합니다.");
            main = False;
            break;
        else:
            print("메뉴에 없는 번호입니다. 다시 선택해주세요");
    else:
        print("잘못된 입력입니다. 다시 선택해주세요");

