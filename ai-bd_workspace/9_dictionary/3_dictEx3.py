dict = {1:"일", 2:"이", 3:"삼", 4:"사"};
print(f"keys() : {dict.keys()}");
print(f"values() : {dict.values()}");
print(f"list(dict) : {list(dict)}");
print(f"list(dict.keys()) : {list(dict.keys())}");
print(f"list(dict.values()) : {list(dict.values())}");

ls = dict.keys();
print(ls);
# print(ls[0]) -> 리스트 형태이지만 리스트가 아님.
ls = list(dict.keys());
print(ls);
print(ls[0]);
