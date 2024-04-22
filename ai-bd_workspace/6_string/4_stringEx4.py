# split() : 공백 문자를 기준으로 문자들을 분리해 List로 반환
str = "바나나 사과 딸기 망고";
print(str);
print(str.split());
# split("문자열") : 문자열을 기준으로 문자들을 분리
str1 = "바나나, 사과, 딸기, 망고";
print(str1);
print(str1.split(", "));
# splitlines() : 행을 기준으로 문자열을 분리
str2 = "바나나\n사과\n딸기\n망고";
print(str2);
print(str2.splitlines());
print(str2.split("\n"));
# '''문장''', """문장""" : 엔터를 친 문장들을 저장할 수 있음
str3 = '''바나나
딸기
사과
망고
''';
print(str3);
print(str3.splitlines());

# 문자열2.join(문자열1) : 문자열1을 문자열2의 각 문자 사이에 붙임
str4 = "**";
str5 = "hello?";
print(str4.join(str5));