cnt = 1;

def func(cnt):
    print(f"지역변수 : {cnt}");
    cnt += 1;

def func1():
    global cnt; # 전역변수를 함수 내에서 편집이 가능하려면 global로 선언해야 한다.
    print(f"전역변수 : {cnt}");
    cnt += 1;

for i in range(5):
    func(i);
    func1();