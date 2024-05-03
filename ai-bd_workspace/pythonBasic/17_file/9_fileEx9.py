# 파일 내용 수정
dir = 'ai-bd_workspace/pythonBasic/17_file'

file = open(dir + '/bbb.txt', 'r', encoding='utf-8');

text = file.readlines();

name = input("이름 입력 : ");

change = '';
for i in text:
    if name in i.split(",")[0]:
        age = input("나이 입력 : ");
        address = input("주소 입력 : ");
        email = input("이메일 입력 : ");
        change += f"{name},{age},{address},{email}\n";
    else:
        change += i;

file.close();


file = open(dir + '/bbb.txt', 'w', encoding='utf-8');
file.write(change);
file.close();