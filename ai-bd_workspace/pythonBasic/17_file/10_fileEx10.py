dir = 'ai-bd_workspace/pythonBasic/17_file'

def add():
    with open(dir + '/bbb.txt', 'a', encoding='utf-8') as f:
        name = input("이름 입력 : ");
        age = input("나이 입력 : ");
        address = input("주소 입력 : ");
        email = input("이메일 입력 : ");

        f.write(f"{name},{age},{address},{email}\n");
        f.close();



def read():
    text = "";
    with open(dir + '/bbb.txt', 'r', encoding='utf-8') as f:
        text = f.readlines();
        for i in text:
            print(i.split(","));
        
        f.close();
    return text;


def mod():
    text = read();
    with open(dir + '/bbb.txt', 'w', encoding='utf-8') as f:
        
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
        
        f.write(change);
        f.close();



def rem():
    text = read();
    with open(dir + '/bbb.txt', 'w', encoding='utf-8') as f:
        
        name = input("이름 입력 : ");
        change = '';
        
        for i in text:
            if name in i.split(",")[0]:
                print(f"{name} 정보 삭제");
            else:
                change += i;
        
        f.write(change);
        f.close();

read();
add();
mod();
rem();

    