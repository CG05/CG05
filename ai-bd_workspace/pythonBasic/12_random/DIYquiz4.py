# 통아저씨
# 구멍 : 20
# from random import choice;

# holeDict = {};
# last = [];
# main = True;

# for i in range(20):
#     holeDict[i] = [" ", "꽝"];
#     last.append(i);
# holeLs = list(holeDict.keys());
# holeDict[choice(holeLs)] = [" ", "당첨"];

# while main:
#     print("="*80);
#     for i in range(20):
#         print(f"{i:^4}",end="");
#     print();
#     for hole in holeDict:
#         print(f"{holeDict[hole][0]:^4}",end="");
#     print();
#     print("="*80);
#     user = int(input("선택 >> "));
#     if holeDict[holeLs[user]][1] == "당첨":
#         print("당신이 당첨되었습니다.")
#         main = False;
#         continue;
#     else:
#         holeDict[holeLs[user]][0] = "X";
#         last.remove(user);
#     com = choice(last);
#     print(f"com은 {com}을 선택했습니다.");
#     if holeDict[holeLs[com]][1] == "당첨":
#         print("컴퓨터가 당첨되었습니다.")
#         main = False;
#     else:
#         holeDict[holeLs[com]][0] = "X";
#         last.remove(com);

# 영단어 맞추기 게임
from random import randrange, choice
wordList = ["culture", "education", "math", "schedule", "route", "gift", "robber"];
hintList = ["문화", "교육", "수학", "예정표", "길", "선물", "재능", "강도"];

rd = randrange(len(wordList));
word = wordList[rd];
hint = hintList[rd];
question = '';
n = [];

while len(n) < (len(word)//2):
    j = randrange(len(word));
    if not j in n:
        n.append(j);


n.sort();

for i in range(len(word)):
    if i in n:
        question += "_";
    else:
        question += word[i];

for i in range(5):
    print(f"단어 뜻 : {hint}");
    print(f"문제 단어 : {question}");

    answer = input("답을 입력 : ");
    if answer == word:
        print("정답입니다.");
    elif i > 1:
        if len(word) > 5:
            n.pop(0);
            question = '';
            for i in range(len(word)):
                if i in n:
                    question += "_";
                else:
                    question += word[i];
        elif len(word) <= 5 and i > 2:
            n.pop(0);
            question = '';
            for i in range(len(word)):
                if i in n:
                    question += "_";
                else:
                    question += word[i];
    else:
        print("틀렸습니다.");