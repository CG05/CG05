#오목

# table = [];
# raw = [];
# for i in range(19):
#   table.append(raw.copy());
#   for j in range(19):
#     table[i].append("□");

# for i in range(20):
#     for j in range(20):
#       if i == 0 and j == 0:
#         print(f"{0:^3}",end=" ");
#       elif i == 0:
#         print(f"{j:^3}",end=" ");
#       elif j == 0:
#         print(f"{i:^3}",end=" ");
#       else:
#         print(f"{table[i-1][j-1]:^3}",end=" ");
#     print();
  
# # [열][행]
# while True:
#   First = True;
#   Second = True;
#   while First:
#     colomn = input("검은 돌을 놓을 열 번호를 입력하십시오 : ");
#     raw = input("검은 돌을 놓을 행 번호를 입력하십시오 : ");
#     if raw.isdigit() and colomn.isdigit() == True:
#       if table[int(colomn) - 1][int(raw) - 1] == "□":
#         table[int(colomn) - 1][int(raw) - 1] = "●"
#         First = False;
#       else:
#         print("이미 돌이 놓인 자리는 놓을 수 없습니다.");
#     else:
#         print("숫자로 입력해야 합니다. 다시 입력해주십시오.");
  

#   for i in range(20):
#     for j in range(20):
#       if i == 0 and j == 0:
#         print(f"{0:^3}",end=" ");
#       elif i == 0:
#         print(f"{j:^3}",end=" ");
#       elif j == 0:
#         print(f"{i:^3}",end=" ");
#       else:
#         print(f"{table[i-1][j-1]:^3}",end=" ");
#     print();
  

#   while Second:
#     colomn = input("흰 돌을 놓을 열 번호를 입력하십시오 : ");
#     raw = input("흰 돌을 놓을 행 번호를 입력하십시오 : ");
#     if raw.isdigit() and colomn.isdigit() == True:
#       if table[int(colomn) - 1][int(raw) - 1] == "□":
#         table[int(colomn) - 1][int(raw) - 1] = "○";
#         Second = False;
#       else:
#         print("이미 돌이 놓인 자리는 놓을 수 없습니다.");
#     else:
#         print("숫자로 입력해야 합니다. 다시 입력해주십시오.");

#   for i in range(20):
#     for j in range(20):
#       if i == 0 and j == 0:
#         print(f"{0:^3}",end=" ");
#       elif i == 0:
#         print(f"{j:^3}",end=" ");
#       elif j == 0:
#         print(f"{i:^3}",end=" ");
#       else:
#         print(f"{table[i-1][j-1]:^3}",end=" ");
#     print();

#   First = True;
#   Second = True;

# MP3 플레이어
# musicList = ["바람기억"];
# curIndex = 0;
# selected = False;
# main = True;
# while main:
#     if selected == False:
#       select = input("1. 재생 2. 정지 3. 다음곡 4. 이전곡 5. 곡 추가 6. 곡 삭제 0. 종료\n>> ");
#       if select.isdigit() == False:
#         print("숫자 키로 입력해주십시오.");
#         continue;
#       elif int(select) < 0 or int(select) > 6 :
#         print("메뉴 중에서 선택해주십시오.");
#         continue;
#       else:
#         selected == True;
#     if select == "1":
#       print("이전에 재생하던 음악을 재생합니다.");
#       print(f"~재생중~ : {musicList[curIndex]}");
#       selected = False;
#       continue;
#     elif select == "2":
#       print("음악을 정지합니다.");
#       selected = False;
#       continue;
#     elif select == "3":
#       print("재생하던 음악의 다음 곡을 재생합니다.");
#       if curIndex + 1 == len(musicList):
#         curIndex = 0;
#       else:
#         curIndex += 1;
#       print(f"~재생중~ : {musicList[curIndex]}");
#       selected = False;
#       continue;
#     elif select == "4":
#       print("재생하던 음악의 이전 곡을 재생합니다.");
#       if curIndex - 1 < 0:
#         curIndex = len(musicList) - 1;
#       else:
#         curIndex -= 1;
#       print(f"~재생중~ : {musicList[curIndex]}");
#       selected = False;
#       continue;
#     elif select == "5":
#       add = input("추가할 음악을 입력해주십시오 : ");
#       print(f"다음 음악이 추가되었습니다 : {add}");
#       musicList.append(add);
#       selected = False;
#       continue;
#     elif select == "6":
#       add = input("삭제할 음악을 입력해주십시오 : ");
#       if musicList.count(add) > 0:
#         print(f"다음 음악이 삭제되었습니다 : {add}");
#         musicList.remove(add);
#       else:
#         print(f"다음 음악이 존재하지 않습니다 : {add}");
#       selected = False;
#       continue;
#     elif select == "0":
#       print("MP3를 종료합니다.");
#       main = False;
  
import copy;

lsOrigin = [[3, 23, 85, 34, 17, 74, 25, 52, 65],
[10, 7, 39, 42, 88, 52, 14, 72, 63],
[87, 42, 18, 78, 53, 45, 18, 84, 53],
[34, 28, 64, 85, 12, 16, 75, 36, 55],
[21, 77, 45, 35, 28, 75, 90, 76, 1],
[25, 87, 65, 15, 28, 11, 37, 28, 74],
[65, 27, 75, 41, 7, 89, 78, 64, 39],
[47, 47, 70, 45, 23, 65, 3, 41, 44],
[87, 13, 82, 38, 31, 12, 29, 29, 80]]
ls = copy.deepcopy(lsOrigin);
raw = 0;
colomn = 0;
rawMax = [0,0,0,0,0,0,0,0,0];
max = 0;
for j in range(9):
    ls[j].sort();

    rawMax[j] = ls[j].pop();

for k in range(9):
  if max < rawMax[k]:
      max = rawMax[k];
      raw = k;


colomn = lsOrigin[raw].index(max);

print(f"{raw+1} {colomn+1}");


