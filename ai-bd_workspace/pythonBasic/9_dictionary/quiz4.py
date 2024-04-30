# 숫자를 5개 입력 - 순위 정하기 큰 수가 1 ~ 제일 작은 수가 5가 되도록
# 4, 5, 9, 1, 3
# 1등 : 9, 2등 : 5, 3등 : 4, 4등 : 3, 5등 : 1

# rank = [];
# number = [];

# for i in range(5):
#     number.append(int(input("정수 입력 : ")));
#     rank.append(1);
#     for j in range(len(number)):
#         if number[i] > number[j]:
#             rank[j] += 1;
#         elif number[i] < number[j]:
#             rank[i] += 1;


# for i in range(5):
#     print(f"{rank}등 : {number[i]}");

# number = [];
# for i in range(5):
#     number.append(int(input("정수 입력: ")));

# for i in range(len(number)):
#     for j in range(i, len(number)):
#         if number[i] < number[j]:
#            number[i], number[j] = number[j], number[i];

# print(number);

number = [];
for i in range(10):
    number.append(int(input("정수 입력: ")));

for i in range(9):
    for j in range(i+1,0,-1):
        if number[j-1] > number[j]:
            number[j-1], number[j] = number[j], number[j-1];

print(number);