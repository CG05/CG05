class ScoreParent:
    name ="";
    kor = 0;
    eng = 0;
    math = 0;
    subNum = 0;
    total = 0;
    avg = 0;

    def getScore1(self):
        self.name = input("이름 입력 : ");
        
        self.kor = int(input("국어 점수 입력 : "));
        self.eng = int(input("영어 점수 입력 : "));
        self.math = int(input("수학 점수 입력 : "));
        self.subNum = 3;
        self.total = self.kor + self.eng + self.math;

    def output(self):
        
        self.avg = self.total/self.subNum;
        print(f"총점 : {self.total}, 평균 : {self.avg}");

class ScoreChild(ScoreParent):
    misic = 0;
    physical = 0;
    def getScore2(self):
        self.music = int(input("음악 점수 입력 : "));
        self.physical = int(input("체육 점수 입력 : "));
        self.total += self.music + self.physical;
        self.subNum += 2;



c1 = ScoreChild();
c2 = ScoreChild();
c1.getScore1();
c1.getScore2();
c2.getScore1();
c2.getScore2();
c1.output();
c2.output();
