ls = [100, "a", 1.234, "안녕하세요", [1, 2, 3]];

print(f"ls출력 : {ls}");
print(f"인덱스 0번 데이터 : {ls[0]}");
print(f"인덱스 1번 데이터 : {ls[1]}");
print(f"인덱스 2번 데이터 : {ls[2]}");
print(f"인덱스 3번 데이터 : {ls[3]}");
print(f"인덱스 4번 데이터 : {ls[4]}");
# print(f"인덱스 5번 데이터 : {ls[5]}");
# list 길이보다 많은 인덱스를 가져오면 : list index out of range 오류 발생
print(f"인덱스 4번 내부 인덱스 0번 데이터 : {ls[4][0]}");
print(f"인덱스 4번 내부 인덱스 1번 데이터 : {ls[4][1]}");
print(f"인덱스 4번 내부 인덱스 2번 데이터 : {ls[4][2]}");

