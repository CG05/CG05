tp = "회사정보", "제품이름", "가격정보", "출시일자";
ls = ["삼성전자", "폴드4", "100만원", "미정"];
for i in range(4):
  print(f"{tp[i]}\t: {ls[i]}");

ls[2] = "140만원";
ls[3] = "2022. 12";

for i in range(4):
  print(f"{tp[i]}\t: {ls[i]}");
