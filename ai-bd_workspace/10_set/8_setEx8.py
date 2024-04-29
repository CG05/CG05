set1 = {1,2,3};

print(set1);
rm = set1.remove(1);
print(set1);
print(rm); # remove는 반환값이 없다.
# set1.remove(5); -> err : 없는 값 삭제시 에러

set2 = {4,5,6};
dc = set2.discard(4);
print(set2);
print(dc); # discard도 반환값이 없다.
# discard는 없는 값도 에러가 나지 않음
set2.discard(9);
print(set2);