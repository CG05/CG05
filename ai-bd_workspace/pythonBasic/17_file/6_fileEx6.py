# 파일에 저장된 내용 출력
file = open('ai-bd_workspace/pythonBasic/17_file/bbb.txt', 'r', encoding='utf-8');

text = file.readlines();

for i in text:
    name, age, address, email = i.split(",");
    print(f"{name}\t{age}\t{address}\t{email}", end="");