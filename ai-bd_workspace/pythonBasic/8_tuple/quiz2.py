ls = [1,2,3,4,5];
num = int(input("검색할 숫자 입력 : "));

for i in range(len(ls)):
  if ls[i] == num:
    print(f"{ls[i]}이 존재합니다");
    break;
else:
  print(f"{num}이 없습니다");