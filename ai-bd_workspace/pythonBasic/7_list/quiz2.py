# list활용 연산식 계산

originEq = input("연산식 입력 : ");
# originEq = "(-13-((6/2)*5))+3*(2/1)"; 

# = -22
# originEq = "(12-3+4/1)*3";
# = 39
# originEq = "12*1+4/2-7";
# = 7
new = "";
levelList = [];
reslist = [0];

for i,s in enumerate(originEq):
    if s.isdigit():
        if new == "" or new == "( ":
            # 시작이 양수면 + 기호 붙여서 시작(통일성)
            new += "+ " + s;
        else:
            new += s;
    elif s == "(":
        new += s + " ";
    else:
        new += " " + s + " ";

levelList.append(new.split());

iBrack = [];

k = 0;
endBracket = -1;
index = [0];
while 0 <= k < len(levelList):
    print(levelList);
    print(k);
    list = levelList[k];
    floor = k;
    endBracket = -k -1;
    while index[floor] < len(list):
        print(levelList);
        
        block = list[index[floor]];
        if block == "(":
            if endBracket < 0:
                bracketFloor = endBracket * (-1) - 1;
            open = 1;
            close = 0;
            r = index[floor] + 1;
            while open > close:
                if list[r] == "(":
                    open += 1;
                elif list[r] == ")":
                    close += 1;
                r += 1;
            endBracket = r;
            if  list[index[floor] + 1].isdigit():
                levelList.append(["+"]);
                levelList[len(levelList) - 1].extend(list[index[floor] + 1 : endBracket - 1]);
            else:
                levelList.append(list[index[floor] + 1 : endBracket - 1]);
            del list[index[floor] : endBracket]
            iBrack.append([index[floor], bracketFloor]);
            print(iBrack);
            reslist.append(0);
            index.append(0);
            k = len(levelList) - 1;
            if levelList[k].count("(") > 0:
                break;
        else:
            index[floor] += 1;
            
            
        if index[floor] == len(list):
            k -= 1;
            index[k] = 0;
            break;
    
k =  len(levelList) - 1;
while k >= 0:
    print(levelList);
    
    list = levelList[k];
    floor = k;

    for f in range(len(index)):
        index[f] = 0;
    
    while index[floor] < len(list):
        block = list[index[floor]];
        if block == "*" or block == "/":
            if block == "*":
                tmp = float(list[index[floor] - 1]) * float(list[index[floor] + 1]);
            if block == "/":
                tmp = float(list[index[floor] - 1]) / float(list[index[floor] + 1]);
            
            for i in range(3):
                del list[index[floor] - 1];
            list.insert(index[floor] - 1, tmp);
            print(list);
            # 삭제 후에 똑같이 index 증가시키면 건너뛰는 문제 발생 -> 삭제시엔 인덱스 증가 X
        else:
            index[floor] += 1;

    for f in range(len(index)):
        index[f] = 0;

    while index[floor] < len(list):
        block = list[index[floor]];
        # 양수 시작이어도 통일시켜놓은 덕에 깔끔하게 계산 가능
        if block == "+":
            reslist[k] += float(list[index[floor] + 1]);
        if block == "-":
            reslist[k] -= float(list[index[floor] + 1]);
        index[floor] += 1;
    print(reslist);
    if k > 0:
        levelList[iBrack[k - 1][1]].insert(iBrack[k - 1][0], reslist[k]);
        if levelList[iBrack[k - 1][1]][0] != "+" and levelList[iBrack[k - 1][1]][0] != "-":
            levelList[iBrack[k - 1][1]].insert(0, "+");
    k -= 1;

print(reslist[0]);
if(eval(originEq) == reslist[0]):
    print("정답입니다");
else:
    print("오답입니다");
        