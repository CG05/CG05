set1 = {1,2,3};
set2 = {"a", "b", "c"};

print(set1);
# set에 set을 합칠 때는 update()
set1.update({3,5,6});
print(set1);
set1.update(set2);
print(set1);