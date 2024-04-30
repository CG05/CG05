menu = "재생", "정지", "다음곡", "이전곡", "곡추가", "곡삭제", "종료";

for i,m in enumerate(menu):
  print(f"{i + 1} : {m}");
select = input("메뉴 번호 입력 : ");