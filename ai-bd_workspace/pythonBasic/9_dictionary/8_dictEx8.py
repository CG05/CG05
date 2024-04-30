ls = [1,2,3,4];
if 1 in ls:
    print("찾았다");

str = "안녕하세요 반갑습니다.";
if "안녕" in str:
    print("찾았다");

ls1 = [[1,2], [3,4]];
# 이차원 List는 안에 있는 각 List를 하나씩 가져와서 찾아야 한다.
if 1 in ls1[0]:
    print("찾았다");

str2 = [["안녕하세요", "반갑습니다"]];
if "안녕" in str2[0]:
    print("찾았다");