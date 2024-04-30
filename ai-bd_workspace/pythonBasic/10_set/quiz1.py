# 문제
# 0~9까지의 숫자 중
# 컴퓨터가 5개의 숫자를 가지고 있다
# 사용자가 입력한 값에서 컴퓨터가 가진 수를 맞추는 게임
# 사용자가 한 번 입력할 때마다 맞춘 수의 갯수를 출력해준다
# 순서와 상관없이 있는 숫자를 맞추는 게임

set = {1,3,5,7,9};
print(f"남은 숫자 갯수 : {len(set)}");
while True:
    user = input("숫자를 골라주세요 (0 ~ 9): ");
    if user.isdigit():
        if (0 <= int(user) < 10):
            user = {int(user)};
            if set.isdisjoint(user):
                print(f"남은 숫자 갯수 : {len(set) - 1}");
                set -= user;
            else : 
                print(f"남은 숫자 갯수 : {len(set)}");
        else:
            print("잘못된 입력입니다.");
    else:
        print("잘못된 입력입니다.");
    if len(set) == 0:
        print("모든 숫자를 찾았으므로 게임이 종료됩니다.");
        break;
