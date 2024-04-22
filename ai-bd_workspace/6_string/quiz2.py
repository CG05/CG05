# 이름, 국어, 영어, 수학 점수를 입력 받고 총점, 평균을 출력하도록 구현
# 점수는 0~100만 가능
# 숫자가 아닌 값을 입력해도 에러 없이 처리되도록 구현

nameIsalpha = False;
korIsdigit = False;
mathIsdigit = False;
engIsdigit = False;

while True:
    if nameIsalpha == False:
        name = input("이름을 입력하시오 : ");
        if name.isalpha() == False:
            print("이름은 한글 혹은 영어만 입력가능합니다.");
            continue;
        else:
            nameIsalpha = True;

    if korIsdigit == False:
        kor = input("국어 점수를 입력하시오 : ");
        if kor.isdigit() == False:
            print("점수는 숫자만 입력가능합니다.");
        elif int(kor) < 0 or int(kor) > 100:
            print("점수는 0~100 사이의 숫자만 입력가능합니다.");
            continue;
        else:
            korIsdigit = True;
    
    if engIsdigit == False:
        eng = input("영어 점수를 입력하시오 : ");
        if eng.isdigit() == False:
            print("점수는 숫자만 입력가능합니다.");
        elif int(eng) < 0 or int(eng) > 100:
            print("점수는 0~100 사이의 숫자만 입력가능합니다.");
            continue;
        else:
            engIsdigit = True;
    
    if mathIsdigit == False:
        math = input("수학 점수를 입력하시오 : ");
        if math.isdigit() == False:
            print("점수는 숫자만 입력가능합니다.");
        elif int(math) < 0 or int(math) > 100:
            print("점수는 0~100 사이의 숫자만 입력가능합니다.");
            continue;
        else:
            mathIsdigit = True;
    else:
        total = int(kor) + int(eng) + int(math);
        avg = total / 3;
        print(f"{name}학생의 총점은 {total}점이고 평균은 {avg:.1f}점입니다.");
        print(f"{name}학생의 점수 입력이 끝났습니다. 다음 학생 순서입니다.");
        nameIsalpha = False;
        korIsdigit = False;
        mathIsdigit = False;
        engIsdigit = False;

    
    


