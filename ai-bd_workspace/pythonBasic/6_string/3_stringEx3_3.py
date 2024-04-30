# strip() : 앞뒤 공백을 제거
# rstrip() : 뒤 공백을 제거
# lstrip() : 앞 공백을 제거
str = " python ";
print(str.strip());
print(str.rstrip());
print(str.lstrip());

# strip("문자열") : 앞뒤 문자열을 제거
str1 = "#애완견";
print(str1.strip("#"));

# replace("기존문자", "변경할문자") : 기존 문자를 변경할 문자로 변경
# 기존 문자의 숫자와 변경할 문자의 숫자는 같지 않아도 됨
str2 = "abcdef";
print(str2.replace("c", "ddd"));

print(str);
print(str1);
print(str2);
# 문자열 함수에서 변경된 내용을 저장하려면 변수에 저장해야 한다.
str2 = str2.replace("c", "d");
print(str2);
