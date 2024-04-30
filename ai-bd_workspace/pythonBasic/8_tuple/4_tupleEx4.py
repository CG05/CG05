tp1 = 1,2,3;
tp2 = 4,5,6;
# tuple끼리의 덧셈은 순서대로 연결함을 의미한다.
tp3 = tp1 + tp2;
tp4 = tp2 + tp1;
print(f"tp1 : {tp1}");
print(f"tp2 : {tp2}");
print(f"tp3 : {tp3}");
print(f"tp4 : {tp4}");
# List도 extend 없이 가능하다.
ls1 = [1,2,3];
ls2 = [4,5,6];
ls3 = ls1 + ls2;
print(ls3);