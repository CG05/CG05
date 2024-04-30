str1 = "Hello";
# upper() : 대문자로 통일
print(str1.upper());
str2 = "heLLo";
# lower() : 소문자로 통일
print(str2.lower());

if str1 == str2:
    print("문자열이 같다");
else:
    print("문자열이 다르다");

if str1.upper() == str2.upper():
    print("문자열이 같다");
else:
    print("문자열이 다르다");

# swapcase() : 대소문자 서로 변경
print(str1.swapcase());
print(str2.swapcase());

# title() : 첫 글자는 대문자, 나머지는 소문자로 통일
print(str1.title());
print(str2.title());

