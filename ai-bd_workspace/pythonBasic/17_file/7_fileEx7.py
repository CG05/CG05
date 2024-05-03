# 입력 내용을 파일에 저장
dir = 'ai-bd_workspace/pythonBasic/17_file'
file = open(dir + '/bbb.txt', 'a', encoding='utf-8');

name = input("이름 입력 : ");
age = input("나이 입력 : ");
address = input("주소 입력 : ");
email = input("이메일 입력 : ");

file.write(f"{name},{age},{address},{email}\n")

file.close();