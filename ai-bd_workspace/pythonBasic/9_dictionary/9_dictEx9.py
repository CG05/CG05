student = {"학번" : 1234, "이름" : "홍길동", "학과" : "컴퓨터공학과"};

key = list(student.keys());
value = list(student.values());

for i in range(len(student)):
    print(f"{key[i]} : {value[i]}");
    print(type(i));
for k, v in student.items():
    print(f"{k} : {v}");