def student(name, kor, eng, math):
    sum = kor + eng + math;
    avg = sum / 3;
    return name, sum, avg;

stu1 = ["홍길동", 100, 90, 80];
stu2 = ["이순신", 90, 90, 80];

stu1Score = student(stu1[0],stu1[1],stu1[2],stu1[3])
stu2Score = student(stu2[0],stu2[1],stu2[2],stu2[3])

print(f"이름 : {stu1Score[0]} 총점 : {stu1Score[1]} 평균 : {stu1Score[2]}");
print(f"이름 : {stu2Score[0]} 총점 : {stu2Score[1]} 평균 : {stu2Score[2]}");


