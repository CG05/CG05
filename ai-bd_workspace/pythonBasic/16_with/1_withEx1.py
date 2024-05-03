class Hello:
    def sayHello(self, name):
        print(f"Hello, {name}");

# 파일 읽어올 때 많이 쓰이는 with절
with Hello() as h:
    # 생성 -> 사용 -> 종료의 라이프사이클을 명확히 해준다
    h.sayHello("홍길동");
    h.sayHello("이순신");
