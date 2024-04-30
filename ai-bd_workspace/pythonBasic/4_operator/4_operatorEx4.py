# 논리 연산자 : 여러 조건에 대해 참과 거짓을 어떻게 연산할지 결정
# and : 두 개 이상의 조건이 모두 참일 때만 참으로 나타낸다.
# or : 두 개 이상의 조건이 모두 거짓일 때만 거짓으로 나타낸다.
# not : 한 개 이상의 조건이 참이면 거짓, 거짓이면 참으로 나타낸다.
num1 = 10;
num2 = 5;
num3 = 1;
print(num1 > num2 and num2 > num3);
print(num1 > num2 and num2 < num3);
print(num1 < num2 and num2 > num3);
print(num1 < num2 and num2 < num3);

print(num1 > num2 or num2 > num3);
print(num1 > num2 or num2 < num3);
print(num1 < num2 or num2 > num3);
print(num1 < num2 or num2 < num3);

print(not(num1 > num2));
print(not(num1 < num2));

# and : 포함 범위로 사용
# or : 제외 범위로 사용