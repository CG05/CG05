set1 = {1,2,3,4,5};
set2 = set([4,5,6,7,8]);

print(type(set1));
print(type(set2));

ls1 = [1,2,3,4,5];
ls2 = [4,5,6,7,8];

print(set1 & set2);
print(set1.intersection(set2));
# 교집합을 만들 수 있다.
# print(ls1 & ls2) -> err

print(set1 | set2);
print(set1.union(set2));
# 합집합도 만들 수 있다.

print(set1 - set2);
print(set2 - set1);
print(set1.difference(set2));
print(set2.difference(set1));
