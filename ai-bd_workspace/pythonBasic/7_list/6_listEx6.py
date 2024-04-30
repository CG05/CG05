ls = [10, 20, 30];
# index() : 데이터의 위치를 출력
print(f"10의 위치 : {ls.index(10)}");
# print(f"40의 위치 : {ls.index(40)}"); -> 없는 데이터는 에러 발생

# insert(인덱스 번호, 데이터) : 인덱스 번호 위치에 데이터를 삽입
ls.insert(1, 200);
print(f"insert 후 ls : {ls}"); 

# remove(데이터) : 해당 데이터를 찾아서 삭제
ls.remove(200);
print(f"remove 후 ls : {ls}");

# extend(list) : list에 list데이터를 추가
ls1 = [10, 20, 10, 30];
ls.extend(ls1);
print(f"extend 후 ls : {ls}");

# count(데이터) : list안에서 데이터의 수를 세어줌
print(f"count(10)한 결과 : {ls.count(10)}");

# clear() : list의 데이터를 초기화
ls.clear();
print(f"clear 후 ls : {ls}");
