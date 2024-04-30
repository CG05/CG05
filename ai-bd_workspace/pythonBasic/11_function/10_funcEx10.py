# 전역변수 선언은 기본적으로 해놔야 한다.

def func():
    global cnt; # 선언이 아닌 cnt를 편집하겠다는 표시
    cnt = 0; # 표시 이후 선언은 가능하다.
    cnt +=1;
    print(f"전역변수 : {cnt}");

func();
print(cnt);