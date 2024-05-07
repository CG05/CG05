# 문제
# 학생 성적 프로그램
# 입력 : 순번, 이름, 국어, 영어, 수학
# 입력 후 연산 : 총점, 평균
# 위의 내용을 score.txt에 저장
# 입력, 검색, 삭제, 수정이 가능하도록
# 출력시 순번, 이름, 총점, 평균 출력
import os

class Student:
    total = 0;
    avg = 0;
    def __init__(self, num, name, kor, eng, math) -> None:
        self.num = num;
        self.name = name;
        self.kor = kor;
        self.eng = eng;
        self.math = math;
        self.calc();
        print(f"{self.name}학생의 점수 입력이 완료되었습니다.");

    def __str__(self):
        return f"{self.num},{self.name},{self.kor},{self.eng},{self.math}"
    
    def getName(self):
        return self.name;

    def calc(self):
        self.total = int(self.kor) + int(self.eng) + int(self.math);
        self.avg = self.total/3;

    def editScore(self, select, score):
        if select == "1":
            self.kor = score;
        if select == "2":
            self.eng = score;
        if select == "3":
            self.math = score;
        
        self.calc();
        print("수정이 완료되었습니다.");

    def info(self):
        return f"{self.num}번 {self.name}학생\n총점 : {self.total}점\n평균 : {self.avg}점";

    def __del__(self):
        print(f"{self.name}학생의 정보가 삭제되었습니다.");


dir = "ai-bd_workspace/pythonBasic/17_file/";
stdLs = [];
numLs = [];

def inputScore(prtstr):
    res = input(prtstr);
    if res.isdigit():
        if 0<= int(res)<=100:
            return res;
        else:
            raise Exception("0~100사이 정수만 입력 가능합니다.");
    else:
        raise Exception("숫자(만 입력 가능합니다.");

def read():
    text = "";
    stdLs = [];
    with open(dir + 'score.txt', 'r', encoding='utf-8') as f:
        text = f.readlines();
        for i in text:
            info = i.split(",")
            student = Student(info[0], info[1], info[2], info[3], info[4]);
            stdLs.append(student);
            numLs.append(info[0]);
        f.close();
    return stdLs;

def write():
    with open(dir + 'score.txt', 'w', encoding='utf-8') as f:
        for std in stdLs:
            f.write(str(std));
        f.close();

menu = "입력", "수정", "삭제", "검색", "전체 출력";
stdLs = read();
main = True;
def seqMenu(select):
    global num;
    if select == "5":
        for stu in stdLs:
            print(stu.info());
        return;
    name = input("학생 이름 입력 : ");
    for i, stu in enumerate(stdLs):
        if name == stu.getName():
            while True:
                try:
                    if select == "1":
                        print("이미 등록된 학생입니다.편집 메뉴로 자동 이동됩니다.");
                        select = "2";
                    if select == "2":
                        print("###### 편집 과목 선택 ######");
                        selectSub = input("1.국어 2.영어 3.수학 0.취소 >> ");
                        if 0 < int(selectSub) < 4:
                            score = inputScore(f"{selectSub} 점수 입력 : ");
                            stu.editScore(selectSub, score);
                        elif selectSub == "0":
                            break;
                        else:
                            raise Exception("잘못된 입력입니다.");
                    elif select == "3":
                        delStu = stdLs.pop(i)
                        del delStu;
                    elif select == "4":
                        print(stu.info());
                    else:
                        raise Exception("잘못된 입력입니다.");
                    return;
                except Exception as e:
                    print(e);
                    break;
            return;
        
    else:
        if select == "1":
            while True:
                try:
                    print("###### 학생 등록 절차 ######");
                    num = input("순번 입력 : ");
                    if not num.isdigit():
                        print("숫자만 입력가능합니다.");
                        continue;
                    elif num in numLs:
                        print("이미 존재하는 순번입니다.");
                        continue;
                    kor = inputScore("국어 점수 입력 : ");
                    eng = inputScore("영어 점수 입력 : ");
                    math = inputScore("수학 점수 입력 : ");
                    
                    newStu = Student(num, name, kor, eng, math);
                    numLs.append(num);
                    stdLs.append(newStu);
                    return;
                except Exception as e:
                    print(e);
                    break;
        else:
            raise Exception(f"{name} 학생을 찾을 수 없습니다.");

for std in stdLs:
    print(std);

while main:
    print("###### 학생 성적 관리 프로그램 ######");
    for i, m in enumerate(menu):
        print(f"{i+1}.{m}",end=" ");
    print("0.종료");
    
    select = input("메뉴 선택 >> ");
    try:
        if select == "0":
            print("프로그램을 종료합니다.");
            write();
            main = False;
        elif select.isdigit():
            if 0 < int(select) < 6:
                seqMenu(select);
            else:
                raise Exception("메뉴에 없는 번호입니다.");
        else:
            raise Exception("잘못 입력하셨습니다.");
    except Exception as e:
        print(e);
    os.system("pause");
    os.system("cls");