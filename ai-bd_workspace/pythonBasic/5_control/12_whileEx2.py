i = 1;
odd, even = 0, 0;
while i <= 10:
    if i%2 == 0:
        even += i;
    else:
        odd += i;
    i += 1;

print(f"1~10의 짝수 합 : {even}");
print(f"1~10의 홀수합 : {odd}");