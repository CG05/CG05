# 은행계좌
class Bank:
    accountNo = 0;
    name = "";
    citizenId = "";
    balance = 0;

    def init(self, accountNo, name, citizenId):
        self.accountNo = accountNo;
        self.name = name;
        self.citizenId = citizenId;

    def deposit(self, money):
        self.balance += money;

    def withdrawal(self, money):
        self.balance -= money;

bankList = [];
startAcc = 10000001;

def findAccNo(accountNo):
    for i in range(len(bankList)):
        if int(accountNo) == bankList[i].accountNo:
            return i;
    else:
        print(f"{accountNo}가 없습니다. 계좌번호를 다시 확인하세요.");
        return None;

def inOutMoney():
    print("### 입금/출금 ###");
    select = input("1.입금 2.출금 : ");
    if select == "1" or select == "2":
        sub = "출금";
        if select == "1":
            sub = "입금";
        accountNo = input("계좌번호 입력 : ");
        id = findAccNo(accountNo);
        if id != None:
            money = input(f"{sub}액 입력 : ");
            if money.isdigit():
                if select == "1":
                    bankList[id].deposit(int(money));
                elif select == "2":
                    bankList[id].withdrawal(int(money));
                print(f"잔액 : {bankList[id].balance}원");
                return;
            else:
                print("숫자만 입력 가능합니다.");
        else:
            print(f"{accountNo}가 없습니다. 계좌번호를 다시 확인하세요.");
    else:
        print("입력한 메뉴 번호가 없습니다.");


menu = "1.입금/출금", "2.이체", "3.잔액조회", "4.계좌개설";
while True:
    for i in menu:
        print(i);
    print("0.종료");
    select = input("메뉴 선택 : ");

    if select == "1":
        inOutMoney();
    
    elif select == "2":
        print("### 이체 ###");
        sender = input("보내시는 분의 계좌번호를 입력 : ")
        senderId = 0;
        receiverId = 0;
        senderId = findAccNo(sender);
        if senderId != None:
            print(f"잔액 : {bankList[senderId].balance}");
        else:
            continue;
        receiver = input("받으시는 분의 계좌번호를 입력 : ");
        receiverId = findAccNo(receiver);
        if receiverId != None:
            print(f"이름 : {bankList[receiverId].name}");
        else:
            continue;
        money = input(f"이체 금액 입력 : ");
        if money.isdigit():
            bankList[senderId].withdrawal(int(money));
            bankList[receiverId].deposit(int(money));
            print(f"잔액 : {bankList[senderId].balance}원");
            print("이체가 완료되었습니다.");
            break;
        else:
            print("숫자만 입력 가능합니다.");
    elif select == "3":
        print("### 잔액조회 ###");
        accountNo = input("조회할 계좌번호를 입력 : ")
        foundId = findAccNo(accountNo);
        if foundId != None:
            print(f"잔액 : {bankList[foundId].balance}원");

    elif select == "4":
        print("### 계좌 개설 ###");
        b = Bank();
        name = input("이름 입력 : ");
        citizenId = input("주민번호 입력 : ");
        b.init(startAcc, name, citizenId);
        print(f"계좌번호 : {startAcc}로 계좌가 개설되었습니다.");
        startAcc += 1;
        bankList.append(b);
    elif select == "0":
        print("프로그램 종료");
        break;
    else:
        print("입력한 메뉴 번호가 없습니다.");