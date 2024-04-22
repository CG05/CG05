name = input("이름 : ");
kor = int(input("국어 점수 : "));
eng = int(input("영어 점수 : "));
math = int(input("수학 점수 : "));

if kor > 100 or eng > 100 or math > 100:
    print("점수는 100점 이하여야 합니다.");
elif kor < 0 or eng < 0 or math < 0:
    print("점수는 0점 이상이어야 합니다.");
else:
    scoreSum = kor + eng + math;
    average = scoreSum / 3;
    print(f"합계 : {scoreSum}점");
    print(f"평균 : {average:.1f}점");

    if average >= 90:
        print(f"{name}님은 A입니다.");
    elif average >= 80:
        print(f"{name}님은 B입니다.");
    elif average >= 70:
        print(f"{name}님은 C입니다.");
    elif average >= 60:
        print(f"{name}님은 D입니다.");
    else:
        print(f"{name}님은 F입니다.");

defFee = 3000;
addFee = 100;
addNum = 0;
length = float(input("거리 입력 : "));
if length <= 0:
    print("거리 입력에 오류가 있습니다. 거리는 0보다 커야 합니다.");
else:
    if length > 30:
        addNum = int(length - 30);
    print(f"요금은 {defFee + addFee * addNum}원입니다.")
   
