# 계산기
# 엔터로 값과 연산자 입력, 등호 입력시 결과값 반환
# 결과값 저장 후 다음 연산에 활용
# 연산자 다음에 연산자, 숫자 다음에 숫자 입력시 오류 반환 후 연산 입력 리셋
# 연산자 외 문자 입력시 오류 반환 후 재입력
# clear 입력시 연산 입력 리셋, reset 입력시 저장된 결과값까지 리셋, exit입력시 종료

# lastInput = "";
# curInput = "";
# eqSave = 0;
# resSave = 0;
# main = True;

# while main:
#     inputStr = input(">> ");
#     if inputStr == "+" or inputStr == "-" or inputStr == "*" or inputStr == "/" or inputStr == "=":
#         if lastInput == "+" or lastInput == "-" or lastInput == "*" or lastInput == "/" or lastInput == "=":
#             print("연산자 다음 바로 연산자가 올 수 없습니다. 입력을 초기화합니다.");
#             lastInput = "";
#             eqSave = 0;
#             continue;
#         else:
#             curInput = inputStr;
#     elif inputStr == "clear":
#         lastInput = "";
#         eqSave = 0;
#         continue;
#     elif inputStr == "reset":
#         lastInput = "";
#         eqSave = 0;
#         resSave = 0;
#         continue;
#     elif inputStr == "exit":
#         main = False;
#         print("계산기를 종료합니다.");
#         break;
#     else:
#         if inputStr.isdigit() == False:
#             print("잘못된 입력입니다. 숫자나 연산자를 입력해주십시오.");
#             continue;
#         elif lastInput.isdigit() == True:
#             print("잘못된 입력입니다. 숫자 다음 바로 숫자가 올 수 없습니다. 입력을 초기화합니다.");
#             lastInput = "";
#             eqSave = 0;
#             continue;
#         else:
#             curInput = inputStr;
    

#     if curInput.isdigit():
#         if lastInput == "":
#             eqSave = float(curInput);
#             resSave = 0;
#         elif lastInput == "+":
#             eqSave += float(curInput);
#         elif lastInput == "-":
#             eqSave -= float(curInput);
#         elif lastInput == "*":
#             eqSave *= float(curInput);
#         elif lastInput == "/":
#             if float(curInput) == 0:
#                 print("잘못된 입력입니다. 0으로 나눌 수 없습니다.");
#                 continue;
#             else:
#                 eqSave /= float(curInput);

#         lastInput = curInput;
#     elif curInput == "=":
#         if lastInput == "":
#             print(f">> {resSave:9f}");
#         else:
#             print(f">> {eqSave:9f}");
#             resSave = eqSave;
#         lastInput = "";
#         eqSave = 0;
#     else:
#         if resSave != 0:
#             eqSave = resSave;
#         lastInput = curInput;


eq = "-13-6/2*5+3"; 
# = -25
# eq = "12-3+4/1*3";
# = 21
# eq = "12*1+4/2-7";
# = 7
new = "";
res = 0;

for i,s in enumerate(eq):
    if s.isdigit():
        if new == "":
            # 시작이 양수면 + 기호 붙여서 시작(통일성)
            new += "+ " + s;
        else:
            new += s;
    else:
        new += " " + s + " ";

list = new.split();

index = 0;
while index < len(list):
    block = list[index];
    print(index);
    tmp = 0;
    if block == "*" or block == "/":
        if block == "*":
            tmp = int(list[index - 1]) * int(list[index + 1]);
        if block == "/":
            tmp = int(list[index - 1]) / int(list[index + 1]);
        
        for i in range(3):
            del list[index - 1];
        list.insert(index - 1, tmp);
        print(list);
        # 삭제 후에 똑같이 index 증가시키면 건너뛰는 문제 발생 -> 삭제시엔 인덱스 증가 X
    else:
        index += 1;

for index, block in enumerate(list):
    # 양수 시작이어도 통일시켜놓은 덕에 깔끔하게 계산 가능
    if block == "+":
        res += int(list[index + 1]);
    if block == "-":
        res -= int(list[index + 1]);

print(res);
        


            



                
        


        

        