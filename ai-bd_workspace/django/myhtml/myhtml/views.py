from django.shortcuts import HttpResponse, render

def main(req):
    sitename = "KG EDU"
    # html = '<body><h1>메인페이지입니다</h1></body>';
    # return HttpResponse();
    content = {
        "sitename" : sitename,
    }
    return render(req, 'main.html', content);

def test1(req):
    content = {
        "키" : "키의 값",
        "num" : 100,
        "float" : 1.1234,
        "string" : "문자열",
        "list" : [10, 20, "리스트"],
        "dict" : {"a" : "A저장", "b" : "B저장"},

    }
    return render(req, 'test1.html', content);

def quiz1(req):
    li = ["강아지", "고양이", "코끼리", "기린", "하마"];
    dict1 = {"구글" : "http://www.google.com", "네이버" : "http://www.naver.com"};
    content = {
        "animals" : li,
        "sites" : dict1
    }
    # quiz1.html에 출력하기
    return render(req, 'quiz1.html', content);\

def test2(req):
    li = ["강아지", "고양이", "코끼리", "기린", "하마"];
    dict1 = {"구글" : "http://www.google.com", "네이버" : "http://www.naver.com"};
    content = {
        "animals" : li,
        "sites" : dict1
    }
    # quiz1.html에 출력하기
    return render(req, 'test2.html', content);

def quiz2(req):
    li = [
        [1,2,3,4,5],
        ["육", "칠", "팔", "구", "10"],
        [11,12,13,14,15]
    ]
    content = {"li" : li};
    # 위의 데이터를 table태그를 이용해 3행 5열로 출력
    return render(req, 'quiz2.html', content);

def test3(req):
    li = [
        [1,2,3,4,5],
        ["육", "칠", "팔", "구", "10"],
        [11,12,13,14,15]
    ]
    content = {"li" : li};
    return render(req, 'test3.html', content);

def test4(req):
    content = {
        "site" : {"구글" : "https://www.google.com"},
        "num1" : 10,
        "num2" : 5,
        "float1" : 10.0,
        "float2" : 5.0,
    };
    return render(req, 'test4.html', content)

def quiz3(req):
    content = {
        "site" : {"네이버" : "https://www.naver.com",
                  "구글" : "https://www.google.com",
                  "다음" : "https://www.daum.net"},
    };
    return render(req, 'quiz3.html', content);

def quiz4(req):
    content = {
        "worldcup": [["순위","국가","승점","승","무","패","득점","실점","골득실"],
                    [1,"이란",17,5,2,0,6,0,6],
                    [2,"대한민국",13,4,1,2,9,7,2],
                    [3,"시리아",8,2,2,3,2,3,-1]],
    }
    return render(req,'quiz4.html', content);
