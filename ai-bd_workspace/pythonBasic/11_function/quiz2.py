# 문제
# 아르바이트 월급 계산기
# 시급 - 기본 : 10000원

# 위의 사람의 월\급을 함수를 만들어서 계산 - 월30일
# 시급과 시간을 입력받고 월급을 계산

def calc(time, pay=10000):
    if time > 24 or time < 0:
        print("시간 또는 시급 입력이 잘못되어 계산할 수 없습니다.");
        return None;
    elif pay < 10000:
        print("시급을 잘못 입력하여 기본 시급 10000원으로 계산합니다.");
        return time * 10000 * 30;

    else:
        return time * pay * 30;

def inputNum(prtStr):
    num = input(prtStr);
    if num.isdigit():
        return int(num);
    else:
        return None;

while True:
    result = 0;
    workPay = inputNum("시급을 입력 : ");
    workTime = inputNum("하루 근로 시간을 입력 : ");
    if workTime == None:
        print("근로 시간을 잘못 입력하셨습니다.");
        continue;
    
    elif workPay == None:
        print("시급을 잘못 입력하여 기본 시급 10000원으로 계산합니다.");
        result = calc(workTime);
    else:
        result = calc(workTime, workPay);

    if result != None:
        print(f"당신의 월급은 {result}원입니다.");
