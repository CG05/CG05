num = {1:"일",2:"이",3:"삼"};
print(f"num : {num}");
print(f"num.get(3): {num.get(3)}");
print(f"num.get(9): {num.get(9)}");
print(f"num.get(0,'없음'): {num.get(0,'없음')}");
print(f"num.get(2,'없음'): {num.get(2,'없음')}");

su = int(input("검색할 키 입력 : "));
if num.get(su) == None:
    print("찾는 값이 없습니다.");
else:
    print(f"num.get(su) : {num.get(su)}");

