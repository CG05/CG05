# 문제
# 학생 성적 프로그램
# 이름, 국어, 영어, 수학, 평균, 총점
# 입력, 수정, 삭제, 검색

class Student:
    # name = "";
    kor = 0;
    eng = 0;
    math = 0;
    total = 0;
    avg = 0;

    def __init__(self, name) -> None:
        self.name = name;
    
    def digitCheck(self, sub):
        score = input(f"{sub} 점수 입력 : ");
        if score.isdigit():
            if 0 <= int(score) <= 100:
                return int(score);
            else:
                print("0~100까지의 정수만 가능합니다.");
                return None;
        else:
            print("숫자만 입력가능합니다.");
            return None;
    
    def calc(self):
        self.total = self.kor + self.eng + self.math;
        self.avg = self.total/3;

    def initScore(self):
        kor = self.digitCheck("국어")
        eng = self.digitCheck("영어")
        math = self.digitCheck("수학")
        if kor == None or eng == None or math == None:
            return;

        self.kor = kor;
        self.eng = eng;
        self.math = math;
    
        self.calc();
        print(f"{self.name}학생의 점수 입력이 완료되었습니다.");

    def editScore(self, select):
        score = None;
        if select == "1":
            score = self.digitCheck("국어")
        if select == "2":
            score = self.digitCheck("영어")
        if select == "3":
            score = self.digitCheck("수학")
        if score == None:
            return;
    
        if select == "1":
            self.kor = score;
        if select == "2":
            self.eng = score;
        if select == "3":
            self.math = score;
        
        self.calc();
        print("수정이 완료되었습니다.");

    def info(self) -> str:
        return f"{self.name}학생의 정보입니다.\n국어 : {self.kor}점\n영어 : {self.eng}점\n수학 : {self.math}점\n총점 : {self.total}점\n평균 : {self.avg}점";

    def __str__(self) -> str:
        return self.name;

    def __del__(self):
        print(f"{self.name}학생의 정보가 삭제되었습니다.");

menu = "입력", "수정", "삭제", "검색";
stuList = []
main = True

def seqMenu(select):
    name = input("학생 이름 입력 : ");
    for i, stu in enumerate(stuList):
        if name == str(stu):
            if select == "1":
                print("이미 등록된 학생입니다.편집 메뉴로 자동 이동됩니다.");
                select = "2";
            if select == "2":
                print("###### 편집 과목 선택 ######");
                selectSub = input("1.국어 2.영어 3.수학 0.취소");
                if 0 < int(selectSub) < 4:
                    stu.editScore(selectSub);
                elif selectSub == "0":
                    return;
            elif select == "3":
                stuList.pop(i)
                print(f"{name}학생의 정보가 삭제되었습니다.");
            elif select == "4":
                print(stu.info());
            return;
    else:
        if select == "1":
            print("###### 학생 등록 절차 ######");
            newStu = Student(name);
            newStu.initScore();
            stuList.append(newStu);
        else:
            print(f"{name} 학생을 찾을 수 없습니다.");


while main:
    print("###### 학생 성적 관리 프로그램 ######");
    for i, m in enumerate(menu):
        print(f"{i+1}.{m}",end=" ");
    print("0.종료");
    
    select = input("메뉴 선택 >> ");
    if select == "0":
        print("프로그램을 종료합니다.");
        main = False;
    elif select.isdigit():
        if 0 < int(select) < 5:
            seqMenu(select);
        else:
            print("메뉴에 없는 번호입니다.");
    else:
        print("잘못 입력하셨습니다.");

