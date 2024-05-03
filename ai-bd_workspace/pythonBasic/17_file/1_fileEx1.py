# open("파일명", "열기옵션")
# 읽기 : 열기옵션=r
file = open('ai-bd_workspace\\pythonBasic\\17_file\\aaa.txt', 'r', encoding='utf-8');

# file.read() : 파일 내용 가져오기
text = file.read();
print(text);