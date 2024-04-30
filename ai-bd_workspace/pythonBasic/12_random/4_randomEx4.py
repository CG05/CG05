import random

ls = ['a', 'b', 'c', 'd', 'e'];
# shuffle : list 안의 값의 위치를 랜덤하게 변경
random.shuffle(ls);
print(ls);
str = "hello";
# random.shuffle(str); string은 그냥은 불가능. 리스트화해야 함.
lsStr = list(str);
random.shuffle(lsStr);
print(lsStr);