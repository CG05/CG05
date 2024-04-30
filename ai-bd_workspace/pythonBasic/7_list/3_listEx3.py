#len() : list나 문자열의 길이
ls = [0, 0, 0, 0];
print(len(ls));

sumData = 0;
for i in range(len(ls)):
  ls[i] = int(input(f"{i+1}번째 정수 입력 : "));
  sumData += ls[i];
print(f"결과값 : {sumData}");