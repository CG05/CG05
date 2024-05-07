import os

class FileStream:
    def __init__(self) -> None:
        self.dir = os.path.dirname(__file__);
        print(self.dir);

    def read(self, fileName):
        try:
            text = "";
            with open(self.dir + fileName, 'r', encoding='utf-8') as f:
                text = f.readlines();
                
                f.close();
            return text;
        except Exception as e:
            print(e);

    def mod(self, fileName,line, idx=None):
        try:
            text = self.read(fileName);
            with open(self.dir + fileName, 'w', encoding='utf-8') as f:
                change = '';
                found = False;
                for i,t in enumerate(text):
                    if idx == i:
                        change += line;
                        found = True;
                    else:
                        change += t;
                if not found:
                    change += line;
                
                f.write(change);
                f.close();
        except Exception as e:
            print(e);

    def delete(self, fileName, idx):
        try:
            text = self.read(fileName);
            with open(self.dir + fileName, 'w', encoding='utf-8') as f:
                change = '';
                
                for i,t in enumerate(text):
                    if idx == i:
                        continue;
                    else:
                        change += t;
                
                f.write(change);
                f.close();
        except Exception as e:
            print(e);
