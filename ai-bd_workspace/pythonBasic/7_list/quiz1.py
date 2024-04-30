ls = [10, 5, 20, 7, 9, 31, 12, 11, 19, 32];
odd = [];
even = [];
oddSum = 0;
evenSum = 0;

for i in range(len(ls)):
  if i % 2 == 0:
    even.append(ls[i]);
    evenSum += ls[i];
  else:
    odd.append(ls[i]);
    oddSum += ls[i];

print(f"odd : {odd}");
print(f"even : {even}");
print(f"홀수 인덱스의 합 : {oddSum}");
print(f"짝수 인덱스의 합 : {evenSum}");

print(f"홀수합과 짝수합의 차 : {oddSum - evenSum}");

inverLs = ls;
print(f"inverLs : {inverLs}");

sortLs = ls;
sortLs.sort();
print(f"sortLs : {sortLs}");

reverseLs = ls;
reverseLs.sort(reverse=True);
print(f"reverseLs : {reverseLs}");
print(f"inverLs : {inverLs}");
print(f"sortLs : {sortLs}");


