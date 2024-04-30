# indexing : 위치 번호로 원하는 값 찾아오는 것
# slicing : 구간으로 원하는 값들 찾아오는 것
# list의 중요한 가능성

ls = [1, 2, 3, 4, 5];
# indexing
print(ls[0]);
print(ls[1]);
# slicing
print(f"ls[0:3] : {ls[0:3]}");
# 시작값이 0이면 생략 가능
print(f"ls[:3] : {ls[:3]}");
# 끝값도 끝이면 생략가능
print(f"ls[3:] : {ls[3:]}");

str = "slicing test"

print(f"str[0:3] : {str[0:3]}");
# 시작값이 0이면 생략 가능
print(f"str[:3] : {str[:3]}");
# 끝값도 끝이면 생략가능
print(f"str[3:] : {str[3:]}");
