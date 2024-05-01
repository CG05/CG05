class Phonebook: # 괄호 생략 가능
    name = "";
    num = "";
    mail = "";
    def getInfo(self):
        self.name = "0"
        print(" ")
        # self.name = input("이름을 입력하세요 : ");
        # self.num = input("전화번호를 입력하세요 : ");
        # self.mail = input("이메일을 입력하세요 : ");
    def output(self):
        print(f"{self.name}의 전화번호는 {self.num}, 이메일은 {self.mail}입니다.");

pbList = [];
for i in range(3):
    ph = Phonebook();
    ph.getInfo();
    pbList.append(ph);

for i in range(3):
    pbList[i].output();