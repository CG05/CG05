st = "It is a fun Python study";

uNum, tNum, spNum, charNum = 0, 0, 0, 0;

for i in st:
    if i == "u":
        uNum += 1;
    elif i == "t":
        tNum += 1;
    elif i == " ":
        spNum += 1;
    else:
        charNum += 1;

charNum = charNum + uNum + tNum;
print(f"u의 개수는 {uNum}개, t의 개수는 {tNum}개, 총 문자 개수는 {charNum}개입니다.");