set1 = {1,2,3,4,5};
set2 = {4,5,6,7,8};
set3 = {1,2,3,4,5};
set4 = {6,7,8,9,10};

# 교집합이 있는지 확인할 수 있다.
if set1.isdisjoint(set2):
    print("set1 과 set2 는 같은 요소가 하나도 없다");
else:
    print("set1 과 set2 는 같은 요소가 하나는 있다");

if set1.isdisjoint(set3):
    print("set1 과 set3 는 같은 요소가 하나도 없다");
else:
    print("set1 과 set3 는 같은 요소가 하나는 있다");

if set1.isdisjoint(set4):
    print("set1 과 set4 는 같은 요소가 하나도 없다");
else:
    print("set1 과 set4 는 같은 요소가 하나는 있다");

