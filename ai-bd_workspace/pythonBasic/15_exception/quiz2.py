# 문제
# 회사 인사 관련 프로그램
# 직책 : 사장, 이사, 부장, 과장, 대리, 사원
# 임직원 : 이름, 주민번호, 이메일, 전화번호
# 인사 등록, 인사 수정, 인사 삭제, 인사 검색
# 등록시: 이름, 주민번호, 이메일, 전화번호, 직책 등록
# 수정시: 이름만, 주민번호만, 이메일만, 전화번호만, 직책만 수정 가능
# 삭제 : 인사 정보 삭제
# 검색 : 이름 검색, 전체 검색
# try-except로 오류 없이 진행되도록
import copy
import os
posLs = "사장", "이사", "부장", "과장", "대리", "사원";
subLs = "사번", "이름", "주민번호", "이메일", "전화번호", "직책";
idNumCnt = 1000; # 사번 카운터
personLs = []; # 인사 리스트

class Person:

    def prtMenu(self, ls):
        for i, v in enumerate(ls):
            print(f"{i}.{v}");
    
    def __init__(self, id) -> None: # 인사 등록시 새 인스턴스 생성하며 실행. 매개변수 id = 주민번호
        self.info = {}; # 정보 딕셔너리
        global idNumCnt; # 사번 카운터를 수정해야 하기 때문에 global
        for sub in subLs:
            if sub == "직책":
                self.prtMenu(posLs); # 직책은 posLs로 번호 출력 후 
                self.info[sub] = posLs[int(input(f"{sub} 번호 입력 : "))]; # 번호 선택하여 입력
            elif sub == "주민번호":
                self.info[sub] = id; # 주민번호는 사전에 매개변수로 받아놓음
            elif sub == "사번":
                self.info[sub] = idNumCnt; # 사번 카운터 적용 
                idNumCnt += 1; # 이후 카운터를 증가시켜 중복될 수 없게 함
            else:
                self.info[sub] = input(f"{sub} 입력 : ");

        
    def modify(self):
        self.prtMenu(subLs);
        sub = subLs[int(input("수정 대상 번호 입력 : "))];
        if sub == "직책":
            self.prtMenu(posLs);
            self.info[sub] = posLs[int(input(f"수정 {sub} 번호 입력 : "))];
        else:
            self.info[sub] = input(f"수정 {sub} 입력 : ");

    def __str__(self):
        outInfo = copy.deepcopy(self.info);
        outId = outInfo["주민번호"][:7];
        outId += "******";
        outInfo["주민번호"] = outId
        return f"{outInfo}"
    
    def name(self):
        return self.info.get("이름");

    def isDuple(self, id): # 주민번호로 중복 확인
        if id == self.info.get("주민번호"):
            return True;
        else:
            return False;

    def isCorrectId(self, idNum): # 중복될 수 없는 사번으로 수정/삭제
        if idNum == self.info.get("사번"):
            return True;
        else:
            return False;
    

def sequence(menuSelect): # 메뉴 선택 후 진행
    global personLs
    try:
        menu = menuLs[menuSelect];
        print(f"###### 인사 {menu} ######");
        if menu == "검색":
            select = int(input("1.이름으로 검색 2.전체 인사에서 검색"));
            if select == 1 or select == 2:
                key = input("검색어 : ");
                count = 0;
                for person in personLs:
                    if select == 1:
                        if key in person.name():
                            print(person);
                            count += 1;
                    else:
                        if key in str(person):
                            print(person);
                            count += 1;
                if count == 0:
                    print("검색된 인사 정보가 없습니다.");
            else:
                raise Exception("없는 메뉴 번호입니다");
        elif menu == "수정":
            id = input("등록된 사번 입력 : ");
            for person in personLs:
                if person.isCorrectId(id):
                    person.modify();
            else:
                print("해당하는 인사 정보가 없습니다.");
        # #
        # 문제있는 곳 : 리스트에 존재하는 모든 Person 인스턴스가 새로 등록한 인스턴스로 덮어씌워진다..?
        # #
        elif menu == "등록":
            id = input("등록할 인사의 주민번호 입력 : "); # 주민번호를 먼저 받는다
            for person in personLs: # 인사 리스트 순회하면서
                if person.isDuple(id): # 주민번호로 중복확인
                    print("해당 인사는 이미 등록된 인사입니다.");
                    break; # 중복이면 등록 중지
            else: # 중복이 아니면
                newPerson = Person(id); # 새 인스턴스 생성 (id)는 __init__매개변수
                personLs.append(newPerson); # 새 인스턴스 인사 리스트에 append
                for i, p in enumerate(personLs): # 오류 확인용 리스트 출력문
                    print(f"{i}. [{p}]");
                print();
                print(f"{newPerson.name()} 님의 인사 정보 등록 완료");
        elif menu == "삭제":
            idNum = input("등록된 사번 입력 : ");
            for i, person in enumerate(personLs):
                if person.isCorrectId(idNum):
                    delPerson = personLs.pop(i)
                    del delPerson;
            else:
                print("해당하는 인사 정보가 없습니다.");
        else:
            raise Exception("없는 메뉴 번호입니다");
    except Exception as e:
        print(f"잘못된 입력입니다 : {e}");

    

menuLs = "등록", "수정", "삭제", "검색";
main = True;
while main:
    try:
        for i, p in enumerate(personLs):
            print(f"{i}. [{p}]");
        print();
        print("###### KG사 인사정보체계 ######");
        for i, m in enumerate(menuLs):
            print(f"{i}. 인사 {m}");
        select = int(input("메뉴 번호 선택 : "));
        sequence(select);
        os.system("pause");
    except Exception as e:
        print(f"잘못된 입력입니다 : {e}");