# 로그인 및 개인 소개 메시지 출력 프로그램
# 메인에서 로그인/회원가입
# 로그인 후 본인 소개 메시지 출력/메시지 수정/타인 메시지 목록 출력/비밀번호수정/회원탈퇴
# 로그인 정보 파일1, 소개 메시지 파일1
import os

class DictFileStream:
    def __init__(self) -> None:
        self.dir = os.path.dirname(__file__);
        print(self.dir);

    def read(self, fileName):
        try:
            dict = {};
            with open(self.dir + fileName, 'r', encoding='utf-8') as f:
                text = f.readlines();
                for i in text:
                    key = i.split(":")[0];
                    value = i.split(":")[1].strip("\n");
                    
                    dict[key] = value;
                f.close();
            return dict;
        except Exception as e:
            print(e);

    def mod(self, fileName, key, value):
        try:
            dict = self.read(fileName);
            with open(self.dir + fileName, 'w', encoding='utf-8') as f:
                change = '';
                found = False;
                for i in dict:
                    if key == i:
                        change += f"{key}:{value}\n";
                        found = True;
                    else:
                        change += f"{i}:{dict.get(i)}\n";
                if not found:
                    change += f"{key}:{value}\n";
                
                f.write(change);
                f.close();
        except Exception as e:
            print(e);

    def delete(self, fileName, key):
        try:
            dict = self.read(fileName);
            with open(self.dir + fileName, 'w', encoding='utf-8') as f:
                change = '';
                
                for i in dict:
                    if key == i:
                        continue;
                    else:
                        change += f"{i}:{dict.get(i)}\n";
                
                f.write(change);
                f.close();
        except Exception as e:
            print(e);

fs = DictFileStream();
userConfig = '\\userConfig.txt';
userInfo = '\\userInfo.txt';
main = True;

def login():
    id = input("아이디 입력 : ");
    pw = input("패스워드 입력 : ");
    config = fs.read(userConfig);
    if id in config:
        if config.get(id) == pw:
            print(f"로그인 성공. 환영합니다, {id}");
            return id;
        else:
            raise Exception("로그인 실패 : pw 오류");
    else:
        raise Exception("로그인 실패 : id 오류");

def signup():
    while True:
        config = fs.read(userConfig);
        id = input("아이디 입력 : ");
        if id in config:
            print("중복된 아이디");
            continue;
        pw = input("패스워드 입력 : ");
        pwRe = input("패스워드 확인 : ");
        if pw != pwRe:
            print("패스워드 재확인 요망");
            continue;
        fs.mod(userConfig, id, pw);
        print("회원가입 완료");
        break;

def myMessage(id):
    info = fs.read(userInfo);
    mine = info.get(id);
    print("="*40);
    if mine == None:
        print("등록된 메시지가 없습니다. 새로 등록해주세요.");
    else:
        print(mine);
    print("="*40);

def modMessage(id):
    info = fs.read(userInfo);
    mine = info.get(id);
    print("="*40);
    print(f"현재 메시지 : {mine}");
    new = input("새로운 메시지를 입력 : ");
    print("-"*40);
    fs.mod(userInfo,id,new);
    print("메시지 수정 완료");

def messageList():
    info = fs.read(userInfo);
    print("="*40);
    for i in info:
        print(f"{i} : {info.get(i)}");
    print("="*40);

def search():
    info = fs.read(userInfo);
    print("="*40);
    id = input("찾을 아이디 입력 : ");
    print("-"*40);
    found = False;
    for i in info:
        if id in i:
            print(f"{i} : {info.get(i)}");
            found = True;
    if not found:
        print("검색 결과가 없습니다.");
    print("="*40);

def signout(id):
    config = fs.read(userConfig);
    print("="*40);
    pw = input("현재 비밀번호 입력 : ");
    if pw == config.get(id):
        print("계정을 삭제합니다.");
        fs.delete(userConfig, id);
        fs.delete(userInfo, id);
    else:
        raise Exception("비밀번호를 확인해주십시오.");


def mainLogin():
    print("###### KG SNS ######");
    select = input("1.로그인 2.회원가입 0.종료\n>> ");
    try:
        if select == "1":
            id = login();
            return id;
        elif select == "2":
            signup();
            return None;
        elif select == "0":
            global main;
            print("프로그램을 종료합니다.");
            main = False;
            return None;
        else:
            raise Exception("잘못된 입력입니다.");
    except Exception as e:
        print(e);
        return None;

def userHome(id):
    while True:
        print(f"###### {id}의 Home ######");
        select = input("1.내 소개메시지 2.소개메시지 등록/수정 3.소개메시지 목록 4.아이디 검색 5.회원탈퇴 0.로그아웃\n>> ");
        try:
            if select == "1":
                myMessage(id);
            elif select == "2":
                modMessage(id);
            elif select == "3":
                messageList();
            elif select == "4":
                search();
            elif select == "5":
                signout(id);
                break;
            elif select == "0":
                print("로그아웃합니다.");
                break;
            else:
                raise Exception("잘못된 입력입니다.");
        except Exception as e:
            print(e);
            continue;
            
while main:
    uid = mainLogin();
    if uid != None:
        userHome(uid);



