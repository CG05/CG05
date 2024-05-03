class Phonebook: # 괄호 생략 가능
    info = {}
    def getInfo(self):

        self.info["name"] = input("이름을 입력하세요 : ");
        self.info["num"] = input("전화번호를 입력하세요 : ");

    def output(self):
        print(f"{self.info["name"]}의 전화번호는 {self.info["num"]}입니다.");

pbList = [];
for i in range(3):
    ph = Phonebook();
    ph.getInfo();
    pbList.append(ph);

for i in range(3):
    pbList[2-i].output();