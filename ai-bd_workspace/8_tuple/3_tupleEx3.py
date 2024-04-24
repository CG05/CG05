tp = 10, 20, 30, "문자열", 1.234;
print(tp);
print(f"tp[0] : {tp[0]}");
print(f"tp[3] : {tp[3]}");

num = tp[0];
print(f"tp[0]에서 가져온 num : {num}");
for i in tp:
	print(i);
# tuple은 데이터를 수정할 수 없어 다음은 오류가 발생
# tp[0] = 10000;
