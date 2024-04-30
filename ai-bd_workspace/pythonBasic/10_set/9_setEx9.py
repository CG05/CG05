set1 = {"b",1,2,3,4,0,"a"};
print(set1);
# 제일 앞의 값을 빼내고 싶으면 pop()
# 저장된 set의 가장 앞의 값
print(f"set1.pop() : {set1.pop()}"); # 빼낸 값을 반환
print(set1);

set2 = {"b", "c", "d", "a"}
print(f"set2.pop() : {set2.pop()}"); # 빼낸 값을 반환
print(set2);
# 비우고 싶다면 clear()
set1.clear();
print(set1);