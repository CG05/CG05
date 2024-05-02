class Test:
    name = "홍길동";

    def output(self):
        print(self.name)

t1 = Test();
t1.output();
t2 = Test();
t2.output();
t3 = Test();
t3.name = "김유신";
t3.output();