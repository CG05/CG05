savedId = "sung";
savedPw = "0105";
inputId = input("아이디 입력 : ");
inputPw = input("비밀번호 입력 : ");

if inputId == savedId:
    if inputPw == savedPw:
        print("로그인에 성공했습니다.");
    else:
        print("비밀번호가 일치하지 않습니다.");
else:
    print("등록되지 않은 아이디입니다.");