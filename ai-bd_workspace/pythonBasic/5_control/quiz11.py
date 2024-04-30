num = int(input("수 입력 (10~20): "));
i = 1;
sum = 0;
# if 10 <= num <= 20:
#     while i <= num:
#         sum += i;
#         i += 1;
#     print(sum);
# else:
#     print("10~20사이의 수를 입력하시오.");
while True:
    num = int(input("수 입력 (10~20): "));
    if 10 <= num <= 20:
        break;
    else:
        sum += i;
    print(sum);