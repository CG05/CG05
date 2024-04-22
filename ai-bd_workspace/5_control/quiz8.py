multi = int(input("원하는 배수 입력 : "));
for i in range(101):
    if i%multi == 0:
        print(i);

start = int(input("첫 번째 수 입력 : "));
end = int(input("두 번째 수 입력 : "));

if start > end:
    start, end = end, start;

sum = 0;
for i in range(start, end):
    sum += i;
print(f"{start}이상 {end}미만의 범위의 합은 {sum}입니다.");

