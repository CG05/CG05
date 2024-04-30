# input() : 키보드로 입력된 값을 파이썬으로 가져오기 위한 함수
inputData = '';

#print함수의 end 옵션은 끝나고 나서 어떻게 할 것인지를 나타낸다.
print("값 입력 : ", end='');
inputData = input();
# input()만 사용하면 입력 대기 상태가 된다.

print(f"입력받은 값 : {inputData}");
