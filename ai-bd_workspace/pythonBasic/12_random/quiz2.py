# 점심 메뉴 랜덤 선택 프로그램
import random
menuKor = ["돼지국밥", "순두부찌개", "김치찌개", "된장찌개"];
menuWes = ["피자", "파스타", "햄버거", "샌드위치"];
menuChi = ["짜장면", "짬뽕", "마라탕", "마라샹궈"];
menuSimple = ["김밥", "라면", "도시락", "계란"];
menu = {"한식" : menuKor, "양식" : menuWes, "중식" : menuChi, "간단한" : menuSimple};

for cat in menu:
    print(f"{cat} 음식 중 오늘의 추천 음식은 {random.choice(menu[cat])}입니다.");


