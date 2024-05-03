# 파일 내용 삭제
dir = 'ai-bd_workspace/pythonBasic/17_file'

file = open(dir + '/bbb.txt', 'r', encoding='utf-8');

text = file.readlines();
# 삭제할 이름 입력
name = input("이름 입력 : ");

change = '';
for i in text:
    if name in i.split(",")[0]:
        print("있음");
    else:
        change += i; # 삭제할 내용 빼고 변수에 저장

file.close();

# 변수의 텍스트를 덮어쓰기
file = open(dir + '/bbb.txt', 'w', encoding='utf-8');
file.write(change);
file.close();