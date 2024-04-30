# isdigit() : 전체가 숫자로 되어있으면 True 아니면 False
while False:
    select = input("1.입력 2.출력 3.수정 4.삭제 0.종료 : ");
    if select.isdigit():
        select = int(select);
        if 0 <= select <= 4:
            print(f"{select} 번을 선택했습니다");
        else:
            print(f"{select} 번은 없는 번호입니다. 다시 입력하세요.");
    else:
        print("숫자를 입력하세요.");

# isalpha() : 전체가 문자로만 되어있으면 True 아니면 False
# 숫자, 기호, 공백을 제외한 한글, 영어 등의 언어문자로만 이루어져야 함
str = "abcde안녕하세요";
if str.isalpha():
    print("문자로만 구성돼있습니다.");

# isalnum() : 전체가 문자와 숫자로 되어있으면 True 아니면 False
str1 = "abcde안녕하세요123";
if str1.isalnum():
    print("문자와 숫자로만 구성돼있습니다.");

# islower(), isupper() : 전체가 소문자(대문자)로 되어있으면 True 아니면 False
# 대소문자가 구분되는 영어에만 해당. 숫자 공백 기호는 무시
str2 = "abcde 12";
str3 = "ABCDE 12";
if str2.islower():
    print("소문자로만 구성돼있습니다.");
if str3.isupper():
    print("대문자로만 구성돼있습니다.");

# isspace() : 전체가 공백문자로 되어있으면 True 아니면 False
str4 = "       ";
if str4.isspace():
    print("공백으로만 구성돼있습니다");
