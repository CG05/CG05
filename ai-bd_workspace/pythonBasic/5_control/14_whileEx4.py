# break : for문이나 while문의 반복 실행 중에 반복을 종료할 때 사용
# continue : for문이나 while문의 반복에서 뒷 코드를 실행하지 않고 건너뛸 때 사용
i = 0;
while True:
    
    if i == 3:
        break;
    i += 1;
    if i == 2:
        continue;
    print(i);

print("while문 종료");