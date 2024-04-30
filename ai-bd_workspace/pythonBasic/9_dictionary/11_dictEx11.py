num = {1:"일", 2:"이", 3:"삼"};

update = {3:"삼", 4:"사"};

print(num);
num.update(update);
print(num);

num.pop(2);
# del num[2];
print(num);
num[2] = "이"
print(num);