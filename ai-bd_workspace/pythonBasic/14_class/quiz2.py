class Phonebook: # 괄호 생략 가능
    info = {};
    
    def getInfo(self):
        name = input("이름을 입력하세요 : ");
        num = input("전화번호를 입력하세요 : ");
        mail = input("이메일을 입력하세요 : ");
        self.info[name] = [num, mail];
        print("등록이 완료되었습니다.");
    
    def setName(self, name):
        if self.search(name):
            nameTo = input("변경할 이름을 입력하세요. 아무것도 입력하지 않으면 삭제합니다. : ");
            if nameTo == "":
                print(f"{name}의 전화번호를 삭제합니다.");
            else:
                tmp = self.info[name];
                self.info.remove(name);
                self.info[nameTo] = tmp;
                print(f"{name}이 {nameTo}로 변경되었습니다.");
            

    def setNum(self,name):
        numTo = input("변경할 전화번호를 입력하세요 : ");
        if self.search(name)[0]:
            self.info[name][0] = numTo;
            print(f"{name}의 이메일이 {self.info[name][1]}로 변경되었습니다.");
            
        else:
            if numTo == "":
                print("변경할 전화번호를 입력하지 않으셨습니다.");

    def setMail(self,name):
        mailTo = input("변경할 이메일을 입력하세요 : ");
        if self.search(name)[0]:
            self.info[name][1] = mailTo;
            print(f"{name}의 전화번호가 {self.info[name][0]}로 변경되었습니다.");
        else:
            if mailTo == "":
                print("변경할 이메일을 입력하지 않으셨습니다.");
            

    def search(self, name=None):
        if name == None:
            name = input("검색할 이름을 입력하세요. 아무것도 입력하지 않으면 전체 전화번호부를 출력합니다. : ");
        if name in self.info or name == "":
            self.output(name);
            return True;
        else:
            print(f"{name}이 전화번호부에 등록되어있지 않습니다.")
            return False;
            
    def output(self, name = ""):
        if name == "":
            print("="*50);
            if len(self.info) == 0:
                print("전화번호부가 비어있습니다.");
            for name in self.info:
                print(f"{name}의 전화번호는 {self.info[name][0]}, 이메일은 {self.info[name][1]}입니다.");
        else:
            print(f"{name}의 전화번호는 {self.info[name][0]}, 이메일은 {self.info[name][1]}입니다.");

    def reset(self):
        print("전화번호부를 초기화합니다.");
        self.info.clear()

main = True;
pb = Phonebook();
setMenu = [pb.setName, pb.setNum, pb.setMail]

def setFunc():
    select = int(input("1.이름 2.전화번호 3.이메일 0.취소 >> "));
    if select == 0:
        print("편집을 취소하고 메인으로 나갑니다.")
    else:
        name = input("편집할 이름을 입력하세요 : ");
        if name == "":
            print("이름을 입력하지 않으셨습니다.");
        else:
            setMenu[select-1](name);

menu = [pb.getInfo, setFunc, pb.search, pb.reset];


while main:
    print("###### 전화번호부 ######")
    select = int(input("1.등록 2.편집 3.검색 4.초기화 0.종료 >> "));
    print("="*50);
    if select == 0:
        main = False;
    else:
        menu[select-1]();