# 파일 탐색기
class CloudExplorer:
    files = {"root":[{"User":[{}, "폴더"]}, "폴더"]};
    curDirKeys = ["root"];

    def __init__(self, id) -> None:
        self.files = {f"root@{id}":[{"User":[{}, "폴더"]}, "폴더"]};
        self.curDirKeys = [f"root@{id}"];
    
    def curDir(self):
        dir = self.files;
        for key in self.curDirKeys:
            dir = dir[key][0];
        return dir;

    def getType(self, name):
        dir = self.curDir();
        return dir[name][1];

    def modify(self, name, type=None, obj=None):
        dir = self.curDir();
        if obj != None:
            res = False;
            if dir.get(name) != None:
                if dir.get(name)[1] == type:
                    if obj == "/del":
                        del dir[name];
                    else:
                        if type == "파일":
                            dir[name] = [obj, type];
                        else:
                            tmp = dir.get(name);
                            del dir[name];
                            dir[obj] = tmp;
                    res = True;
            else:
                dir[name] = [obj, type];
                res = True;
            
            return res;
        else:
            ls = list(dir.keys());
            res = [];
            for k in ls:
                if name in k:
                    if type == None:
                        res.append(k);
                    else:
                        if dir.get(k)[1] == type:
                            res.append(k);
            return res;

    def inputTypeName(self, seq):
        type = input(f"{seq}할 타입을 선택 1.폴더 2.파일 그 외.취소 >> ");
        if type == "1":
            type = "폴더";
        elif type == "2":
            type = "파일";
        else:
            return None, type;
        name = input(f"{seq}할 {type}의 이름을 입력 >> ");
        print(f"현재 폴더에서 {type}의 {name}을 {seq}합니다.");
        return name, type;

    def inputText(self, seq, type):
        text = input(f"{seq}할 {type}의 텍스트 입력 >> ");
        return text;

    def create(self):
        seq = "생성"
        name, type = self.inputTypeName(seq);
        if name == None:
            return False;
        else:
            res = True;
            if type == "폴더":
                res = self.modify(name, type, {});
            elif type == "파일":
                res = self.modify(name, type, "");
            print(f">> {seq} 작업 진행 성공 : {res}");
            return res;

    def update(self, name):
        seq = "수정"
        if name == None:
            return False;
        else:
            type = self.getType(name);
            res = True;
            if type == "폴더":
                res = self.modify(name, type, self.inputText(seq, type));
            elif type == "파일":
                res = self.modify(name, type, self.inputText(seq, type));
            print(f">> {seq} 작업 진행 성공 : {res}");
            return res;

    def ls(self):
        dir = self.curDir();
        dirKeys = list(dir.keys());
        for key in dirKeys:
            if dir.get(key)[1] == "폴더":
                print(f"{key}/",end=" ");
            elif dir.get(key)[1] == "파일":
                print(f"{key}.txt",end=" ");
        print();
        return True;
    
    def delete(self):
        seq = "삭제"
        name, type = self.inputTypeName(seq);
        if name == None:
            return False;
        else:
            res = True;
            res = self.modify(name, type);
            return res;

    def read(self, fileName):
        dir = self.curDir();
        return dir.get(fileName)[0];

    def curPath(self):
        for key in self.curDirKeys:
            print(f"{key}/",end="");
        print(">> ",end="");

    def toPath(self, to):
        res = False;
        dir = self.curDir();
        dirKeys = list(dir.keys());
        if to in dirKeys:
            if dir.get(to)[1] == "폴더":
                self.curDirKeys.append(to);
            elif dir.get(to)[1] == "파일":
                print(self.read(to));
                res = True;
        elif to == "..":
            print(self.curDirKeys.pop());
        return res;

        

        
main = True;
users = {}
while main:
    userCloud = CloudExplorer;
    print("###### KGOS ######");
    id = input(">> id : ");
    pw = input(">> pw : ");
    if id not in users:
        print(f">> 신규 이용자 {id}님, 환영합니다. 클라우드를 초기화합니다.");
        newCloud = CloudExplorer(id);
        users[id] = [pw, newCloud];
    else:
        if pw == users[id][0]:
            print(f">> {id}님, 환영합니다. 사용환경을 로드합니다.");
            userCloud = users[id][1];
        else:
            print("비밀번호 오류입니다.");
            continue;
    userCloud = users.get(id)[1];
    while True:
        userCloud.curPath();
        cli = input();
        if cli == "ls":
            userCloud.ls();
        elif cli.startswith("./"):
            to = cli.replace("./", "");
            res = userCloud.toPath(to);
            while res:
                inline = input(f"{to} >>> ");
                if inline == "exit":
                    res = False;
                else:
                    userCloud.update

        elif cli == "new":
            userCloud.create();
        elif cli == "del":
            userCloud.delete();
        else:
            print("error : command no support");

