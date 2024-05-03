# 이어쓰기 : 열기옵션=a
file = open('ai-bd_workspace\\pythonBasic\\17_file\\aaa.txt', 'a', encoding='utf-8');

file.write("5번째 줄\n");
file.write("6번째 줄\n");

file.close();

file = open('ai-bd_workspace\\pythonBasic\\17_file\\aaa.txt', 'r', encoding='utf-8');
print(file.readlines());
