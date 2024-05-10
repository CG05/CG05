loginPath = "ai-bd_workspace\\pythonBasic\\18_final\\member.txt"
diaryPath = "ai-bd_workspace\\pythonBasic\\18_final\\diary\\"
from datetime import datetime
import os
import calendar

def main(id):
    now1 = datetime.today()
    today = now1.strftime("%Y-%m-%d");
    year = now1.year;
    month = now1.month;
    logPath = diaryPath + id + "\\";
    os.makedirs(logPath,exist_ok=True);
    while True:
        print("### 일기장 ###");
        print(f"{id}님 환영합니다.");
        print("1. 일기 쓰기");
        print("2. 일기 보기");
        print("3. 달력 보기");
        print("0. 로그아웃");
        select = input("선택 : ");

        if select == "1":
            print("### 일기 쓰기 ###");
            text = [];
            print("일기를 작성하세요. 작성이 완료되면 Ctrl + Z를 눌러 종료하시면 됩니다.");
            while True:
                try:
                    text.append(input());
                except:
                    break;
            print(text);
            with open(logPath + today + ".txt", 'a', encoding='utf-8') as f:
                now = datetime.today()
                f.write(f"\n{now}\n");
                for i in text:
                    f.write(i + "\n");

        elif select == "2":
            print("### 일기 보기 ###");
            diaryList = os.listdir(logPath);
            for i, d in enumerate(diaryList):
                print(f"{i+1}. {d}");
            sub = input("선택 : ");
            if sub.isdigit():
                if 0 < int(sub) <= len(diaryList):
                    with open(logPath + diaryList[int(sub)-1], 'r', encoding='utf-8') as f:
                        text = f.readlines();
                        for t in text:
                            print(t,end="");
                else:
                    print("없는 선택 번호입니다.");
            else:
                print("선택은 숫자만 가능합니다.");
        
        elif select == "3":
            print("### 달력 보기 ###");
            print(f"1. {year}년 달력");
            print(f"2. {year}년 {month}월 달력");
            y = year;
            mon = month;
            sub = input("선택 : ");
            cal = calendar.TextCalendar(firstweekday=6);
            if sub == "1":
                cal.pryear(year);
            elif sub == "2":
                while True:
                    cal.prmonth(y, mon, w=5,l=2);
                    print("이전 - 이전 달");
                    print("다음 - 다음 달");
                    print("종료 - 끝내기");
                    choice = input("선택 : ");
                    if choice == "이전":
                        mon -= 1;
                        if mon == 0:
                            mon = 12;
                            y -= 1;
                    elif choice == "다음":
                        mon += 1;
                        if mon == 13:
                            mon = 1;
                            y += 1;
                    elif choice == "종료":
                        break;
                    else:
                        print("잘못된")
            else:
                print("선택된 메뉴 번호가 없습니다.");
        elif select == "0":
            print("로그아웃되었습니다. 메인 메뉴로 나갑니다.");
            return;
        else:
            print("선택된 메뉴 번호가 없습니다.")

