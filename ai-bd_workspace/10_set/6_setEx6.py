set1 = {1,2,3};
# set1 += {4} -> err : + 불가능
# 요소의 추가는 add()
set1.add(4);
print(set1);
# 이미 존재하는 값은 에러는 나지 않지만 추가되지 않는다.
set1.add(4);
print(set1);

set1.add('4');
print(set1);
set1.add('4');
print(set1);