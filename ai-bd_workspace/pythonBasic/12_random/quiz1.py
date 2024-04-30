# 가위바위보 게임
# from random import randrange

# ls = ["가위", "바위", "보"];

# count = 5;

# def winner(user, com):
#     isWin = True;
#     res = "";
#     if user == com:
#         isWin = False
#         res = "비겼습니다.";
#     elif user < com:
#         if user == 0 and com == 2:
#             res = "user";
#         else:
#             res = "com";
#     elif user > com:
#         if com == 0 and user == 2:
#             res = "com";
#         else:
#             res = "user";
#     return isWin, res;

# def printResult(user):
#     global count;
#     com = randrange(0,3);
#     resIsWin, resWinner = winner(user, com);
#     print(f"user : {ls[user]}, com : {ls[com]}으로 ",end="");
#     if resIsWin:
#         print(f"{resWinner} 승입니다.");
#         count -= 1;
#     else:
#         print(f"비겼습니다.");

# def getUser():
#     user = input("0: 가위 1: 바위 2: 보 >> ");
#     if user.isdigit():
#         if 0 <= int(user) < 3:
#             return int(user);
#         else:
#             return None;
#     else:
#         return None;

# while count > 0:
#     user = getUser();
#     if user != None:
#         printResult(user);
#         print(f"남은 승리 횟수 : {count}");
#     else:
#         print("잘못 입력하셨습니다.");

# 로또
from random import randrange

numSet = set();
while len(numSet) < 6:
    numSet.add(randrange(1,46));

print(numSet);
    
