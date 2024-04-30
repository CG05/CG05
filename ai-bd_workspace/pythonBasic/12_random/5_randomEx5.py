import random as rd
strList = ["hello", "sea", "join", "song", "test", "absolute"];

while True:
    n = rd.randrange(len(strList));
    str = list(strList[n]);
    
    rd.shuffle(str);
    print(f"정답 {len(strList[n])}자");
    for i in str:
        print(i, end=" ");

    result = input("정답 입력 : ");
    if strList[n] == result:
        print("정답입니다");
    else:
        print("오답입니다");