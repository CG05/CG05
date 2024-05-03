try:
    num = int(input("정수 입력 : "));
    print(num*num);
    print(num/num);
except ValueError as e:
    print(f"예외발생 : {e}");
    print("정수만 입력 가능합니다.");
except ZeroDivisionError as e:
    print(f"예외발생 : {e}");
    print("0으로 나눌 수 없습니다.");
except Exception as e:
    print(f"예외발생 : {e}");
finally: # try-except문이 종료되면 반드시 실행
    print("예외처리 종료");
