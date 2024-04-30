num = {1:"일", 2:"이", 3:"삼"};

num[4] = "사";
print(num);
num[4] = "4";
num.setdefault(5,"오");
print(num);
num.setdefault(5,"5");
print(num);