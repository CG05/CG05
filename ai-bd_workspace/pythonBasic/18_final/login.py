# 로그인 한 사람만 접근 가능
# 로그인 한 자신의 폴더에 접근 가능해서 일기쓰기와 보기
import diary
loginPath = "ai-bd_workspace\\pythonBasic\\18_final\\member.txt"
diaryPath = "ai-bd_workspace\\pythonBasic\\18_final\diary\\"

# 로그인, 회원가입
while True:
    print("1.로그인");
    print("2.회원가입");
    print("0.프로그램 종료");
    select = input("선택 : ");

    if select == "1":
        print("### 로그인 ###");
        id = input("아이디 입력 : ");
        pwd = input("암호 입력 : ");

        with open(loginPath, 'r', encoding='utf-8') as f:
            member = f.readlines();
            for m in member:
                m = m.split(",");
                if id == m[0]:
                    if pwd == m[1]:
                        print("로그인 성공");
                        diary.main(id);
                        break;
            else:
                print("아이디나 암호가 틀립니다.");

    elif select == "2": # 아이디, 패스워드, 이름, 이메일
        print("### 회원가입 ###");
        id = "";
        try:
            while True:
                print("회원가입 취소는 Ctrl + Z를 입력");
                id = input("아이디 입력 : ");
                with open(loginPath, 'r', encoding='utf-8') as f:
                    member = f.readlines();
                    for m in member:
                        m = m.split(",");
                        if id == m[0]:
                            print("중복된 아이디입니다. 다시 입력하세요.");
                            break;
                    else:
                        break;
            pwd = input("암호 입력 : ");
            name = input("이름 입력 : ");
            email = input("이메일 입력 : ");
        
            with open(loginPath, 'a', encoding='utf-8') as f:
                f.write(f"{id},{pwd},{name},{email}\n");
    
        except EOFError:
            print("회원가입이 취소되었습니다.");

    elif select == "0":
        print("프로그램 종료");
        break;
    else:
        print("선택된 메뉴 번호가 없습니다");