# 쓰기 : 열기옵션=w
file = open('ai-bd_workspace\\pythonBasic\\17_file\\aaa.txt', 'w', encoding='utf-8');

# file.write() : 파일 내용을 새 입력 내용으로 덮어쓴다.
text = file.write("1번째 줄\n");
text = file.write("2번째 줄\n");
text = file.write("3번째 줄\n");

# 반드시 행동이 끝나면 닫아서 저장해야 한다.
file.close();

# 열어보려면 다시 open해야 한다.
file = open('ai-bd_workspace\\pythonBasic\\17_file\\aaa.txt', 'r', encoding='utf-8');
text = file.readlines();
print(text);