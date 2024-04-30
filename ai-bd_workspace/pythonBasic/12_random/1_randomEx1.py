# random : 난수를 발생시키는 내장모듈
# 모듈을 import해서 사용한다
import random;

# 난수는 0초과 1미만의 소숫점 값을 반환
print(random.random());

# 정수형 난수 (0~99)
print(int(random.random()*100));
# 1~100
print(int(random.random()*100)+1);

