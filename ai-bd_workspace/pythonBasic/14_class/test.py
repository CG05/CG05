# class Test:
#     name = "";
#     def __init__(self, name) -> None:
#         self.name = name;

#     def __del__(self):
#         return print(f"{self.name} deleted.");
# t1 = Test("1")
# t2 = Test("2")
# t3 = Test("3")
# t4 = Test("4")
# t5 = Test("5")
# ls = [t1,t2,t3,t4,t5];

# for i, s in enumerate(ls):
#     if s.name == "3":
#         delete = ls.pop(i);
#         del delete;
#         break;

# print(len(ls));
# 

# class Test:
#     def __init__(self, name):
#         self.name = name

#     def __del__(self):
#         print(f"{self.name} deleted.")

# # 객체 생성
# t1 = Test("1")
# t2 = Test("2")
# t3 = Test("3")
# t4 = Test("4")
# t5 = Test("5")
# ls = [t1, t2, t3, t4, t5]

# import copy;
# # 특정 객체 참조 삭제
# l = copy.deepcopy(ls);
# for i, s in enumerate(l):  # 복사본을 순회
#     if s.name == "3":
#         delete = l.pop(i)
#         del delete  # 여기서 바로 삭제되도록 참조 제거

# ls = l;
# print(len(ls))  # 업데이트된 리스트 길이 출력

