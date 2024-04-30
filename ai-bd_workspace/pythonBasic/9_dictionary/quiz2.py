# 전화번호부 만들기
# 1. 연락처 저장
# 2. 연락처 검색
# 0. 프로그램 종료
menu = "1. 연락처 목록", "2. 연락처 저장", "3. 이름으로 검색", "4. 번호로 검색", "0. 프로그램 종료";
phonebook = {};
main = True;
while main:
    for m in menu:
        print(m,end=" ");
    print();
    select = input("메뉴에서 선택해주십시오 : ");
    if select.isdigit():
        if select == "1":
            print("=========목록=========");
            for i, name in enumerate(phonebook):
                print(f"<{i+1}> {name}\t: {num}");
            print("="*20);
            print("편집하시려면 해당 연락처의 이름을 입력하세요. 메뉴로 나가시려면 0을 입력하세요.");
            edit = input(">> ");
            if edit == "0":
                continue;
            else:
                if edit in phonebook:
                    editNum = input("수정할 연락처를 입력하세요. 취소하시려면 #를, 삭제하시려면 0을 입력하세요. : ");
                    if editNum == "#":
                        print("취소되었습니다. 메뉴로 나갑니다.");
                    elif editNum == "0":
                        print(f"{edit}의 연락처가 삭제되었습니다.");
                        del phonebook[edit];
                    else:
                        print(f"{edit}의 연락처가 {editNum}으로 수정되었습니다.");
                        phonebook[edit] = editNum;
                else:
                    print("해당하는 연락처가 없습니다.");
        elif select == "2":
            num = input("저장할 연락처를 입력해주세요 : ");
            name = input("저장할 이름을 입력해주세요 : ");
            phonebook[name] = num;
            print(f"{name}의 연락처가 저장되었습니다.");
        elif select == "3":
            rName = input("검색할 이름을 입력해주세요 : ");
            if rName in phonebook:
                print(f"{rName} : {phonebook[name]}");
            else:
                print("해당하는 연락처가 없습니다.");
        elif select == "4":
            rNum = input("검색할 연락처를 입력해주세요 : ");
            for name in phonebook:
                if rNum == phonebook[name]:
                    print(f"{name} : {rNum}");
            else:
                print("해당하는 연락처가 없습니다.");
        elif select == "0":
            print("프로그램을 종료합니다.");
            main = False;
            break;
        else:
            print("메뉴에 없는 번호입니다. 다시 선택해주세요");
    else:
        print("잘못된 입력입니다. 다시 선택해주세요");

