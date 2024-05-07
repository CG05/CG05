# 제품등록, 제품출력, 제품검색, 제품 재고 수정
# 인덱스,종류,이름,개수
from random import randrange as rr;
from fs import FileStream;

db = '\\productDB.txt';
fs = FileStream();
sub = "물품번호","종류","이름","개수"
main = True;

def getDB():
    text = fs.read(db);
    pdList = []
    for t in text:
        pdList.append(t.split(","));
    print(pdList);
    return pdList;
    
    
def toDB(list,idx=None):
    line = f"{list[0]},{list[1]},{list[2]},{list[3]}";
    fs.mod(db,line,idx);

def stockIn():
    try:
        category = input("제품 종류 입력 : ");
        name = input("제품 이름 입력 : ");
        count = int(input("제품 수량 입력 : "));
        pdList = getDB();
        for pd in pdList:
            if pd[2] == name:
                raise Exception("중복된 제품이 있습니다. 재고를 수정해주세요")
        else:
            newpd = [rr(1,999999),category,name,count];
            toDB(newpd);
    except Exception as e:
        print(e);

def prtStock():
    pdList = getDB();
    for pd in pdList:
        print(f"{pd[0]:>06}_{pd[1]}_{pd[2]} - {pd[3]}");

def search():
    key = input("검색어 입력 : ");
    pdList = getDB();
    found = False;
    for pd in pdList:
        if key in pd[0] or key in pd[1] or key in pd[2]:
            print(f"{pd[0]:>06}_{pd[1]}_{pd[2]} - {pd[3]}");
            found = True;
    if not found:
        print("검색된 제품이 없습니다.");

def getCount():
    try:
        num = int(input("재고를 수정할 물품번호 입력 : "));
        pdList = getDB();
        for i, pd in enumerate(pdList):
            if num == int(pd[0]):
                print(f"{pd[0]:>06}_{pd[1]}_{pd[2]} - {pd[3]}");
                newCount = int(input("수정할 재고 수량을 입력 : "));
                pd[3] = newCount;
                toDB(pd, i);
                break;
        else:
            print("검색된 제품이 없습니다.");
        
    except Exception as e:
        print(e);


while main:
    print("====== KG 재고관리 ======");
    select = input("1.제품등록 2.제품목록 3.제품검색 4.재고수정 0.종료");
    try:
        if select == "1":
            stockIn();
        elif select == "2":
            prtStock();
        elif select == "3":
            search();
        elif select == "4": 
            getCount();
        elif select == "0":
            print("프로그램 종료");
            main = False;
        else:
            raise Exception("잘못된 입력입니다.");
    except Exception as e:
        print(e);
