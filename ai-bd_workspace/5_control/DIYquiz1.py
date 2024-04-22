# # 1~100 삼육구 게임
# for i in range(1000):
#     a = i//100;
#     b = (i - a*100)//10;
#     c = i%10;

#     if a > 0 and a%3 == 0:
#         print("짝", end="");
#     elif a > 0:
#         print(a, end="");
       
#     if b > 0 and b%3 == 0:
#         print("짝", end="");
#     elif b > 0 or a > 0:
#         print(b, end="");

#     if c > 0 and c%3 == 0:
#         print("짝");
#     else:
#         print(c);

# # 마름모하트♡
# len = 25;
# for i in range(len * 2):
#     if i <= len:
#         for j in range(len - i):
#             print(" ", end=" ");
#         for k in range(i):
#             print(" ♡ ", end=" ");
#         print();
#     else:
#         for j in range(i - len):
#             print(" ", end=" ");
#         for k in range(len*2 - i):
#             print(" ♡ ", end=" ");
#         print();

# 행맨
str = "square";
strLen = len(str);
corrector = 0;

for k in range(strLen):
    print("_",end="");
print(corrector);


for i in range(7):
    print(f"남은 기회 : {7 - i}",end=" ");
    inputSpell = input("입력 : ");

    index = strLen - 1;
    for char in str:
        if char == inputSpell:
            if corrector%(10**(index+1)) - 10**index < 1:
                corrector += 10**index;
                i -= 1;
        if corrector%(10**(index+1)) - 10**index > 0:
            print(char,end="");
        else:
            print("_",end="");
        
        index -= 1;
    print(corrector);

# # 숫자야구
# com = "876";

# for i in range(10):
#     user = input("정답 입력 : ");
#     strike = 0;
#     ball = 0;
#     for j in range(3):
#         for k in range(3):
#             if j == k and com[j] == user[k]:
#                 strike += 1;
#             elif j != k and com[j] == user[k]:
#                 ball += 1;
#     if strike == 0 and ball == 0:
#         print("아웃입니다.");
#     elif strike == 3:
#         print("정답입니다.");
#         break;
#     else:
#         print(f"{strike} 스트라이크, {ball} 볼");