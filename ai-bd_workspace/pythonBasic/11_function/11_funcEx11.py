def func(num):
    return num * num;

# 함수를 변수에 저장해서 사용할 수 있다
f = func;
print(f(3));
ls = [func, 4];
print(ls[0](ls[1]));
dict = {"함수":func,"값":10};
print(dict["함수"](dict["값"]));