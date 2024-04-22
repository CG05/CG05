str = "NeVer EvEr give up"
res = str.title();
print(res.replace(" ", "-"));

str = "2020/01/23";
list = str.split("/");
for s in list:
    print(s);
lsDate = str.split("/");
# enumerate
for i, s in enumerate(lsDate):
    # i에는 인덱스번호, s에는 값이 들어감
    print(f"{i} 인덱스 번호 : {s}");

for i, s in zip(range(len(lsDate)), lsDate):
    print(f"{i} 인덱스 번호 : {s}");
