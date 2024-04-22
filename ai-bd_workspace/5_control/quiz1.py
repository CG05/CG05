num = int(input("정수를 입력하시오 : "));
if num % 3 == 0 :
    print(f"{num}(은)는 3의 배수입니다.");
print("1번 종료");

num1 = int(input("첫 번째 정수를 입력하시오 : "));
num2 = int(input("두 번째 정수를 입력하시오 : "));
if num1 > num2 :
    print(f"{num1}(이)가 더 큽니다.");
if num1 < num2 :
    print(f"{num2}(이)가 더 큽니다.");
print("2번 종료");

num1 = int(input("첫 번째 정수를 입력하시오 : "));
num2 = int(input("두 번째 정수를 입력하시오 : "));
if (num1 + num2) % 2 == 0 and (num1 + num2) % 3 == 0 :
    print(f"합은 {num1 + num2}(으)로 짝수이고 3의 배수입니다.");
print("3번 종료");