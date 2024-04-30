navi = {};
name = "";
menu = "목적지 등록", "목적지 수정", "목적지 검색", "종료";
main = True;

def findName():
    global name;
    name = input("목적지 이름 입력 : ");
    if navi.get(name) == None:
        return False;
    else:
        return True;

def getAddress():
    global navi;
    address = input("목적지 주소 입력 : ");
    navi[name] = address;
    return address;

def append():
    print("#### 목적지 등록 ####");
    if not findName():
        getAddress();
        print(f"{name} 목적지를 등록했습니다.");
    else:
        print(f"{name} 목적지는 이미 등록 되었습니다.");

def update():
    print("수정할 ",end="");
    if not findName():
        print(f"{name} 목적지는 등록되어 있지 않습니다.");
    else :
        print("수정할 ",end="");
        address = getAddress();
        print(f"{name} 목적지의 주소를 {address} 로 변경되었습니다.");

def search():
    print("검색할 ",end="");
    if not findName():
        print(f"{name} 목적지는 등록되어 있지 않습니다.");
    else:
        print(f"{name} 목적지의 주소는 {navi.get(name)} 입니다.")

funcList = [append, update, search];

def selectSequence(selectNum):
    global main;
    if selectNum.isdigit():
        if 0 < selectNum < 4:
            funcList[int(selectNum - 1)]();
        elif selectNum == "4":
            print("프로그램을 종료합니다.");
            main = False;
    else:
        print("없는 메뉴 번호 입니다. 다시 입력 하세요");

def selectMenu():
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}");
    return input("메뉴 번호 선택 : ");

while main: 
    selectSequence(selectMenu());
