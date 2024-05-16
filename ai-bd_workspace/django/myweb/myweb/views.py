from django.http import HttpResponse

# url dispatcher에서 전달받은 함수는 request를 매개변수로 받는다
# request : 요청에 대한 정보가 들어있다.
def test(request):
    return HttpResponse("테스트페이지입니다.")

def pattern1(request,name):
    print(type(name));
    return HttpResponse(f"{name} Test1");

def pattern2(request, name):
    print(type(name));
    return HttpResponse(f"{name} Test2");

def pattern3(request, name):
    print(type(name));
    return HttpResponse(f"{name} Test3");

def quiz1(request, lang):
    # path의 url pattern은 변수명과 함수의 변수명이 같아야 한다.
    lang_code = {"ko":"한국어", "en":"영어", "jp":"일본어"};

    if lang in lang_code:
        return HttpResponse(f"{lang_code[lang]} 페이지");
    else:
        return HttpResponse(f"없는 언어 페이지");

def pattern4(request, lang):
    # re_path에서는 값을 선택해서 처리할 수 있고 함수의 변수명을 마음대로 지정할 수 있다.
    lang_code = {"ko":"한국어", "en":"영어", "jp":"일본어"};

    return HttpResponse(f"{lang_code[lang]} 페이지");
    
def regex1(request, txt):
    return HttpResponse(f"{txt} 데이터 출력");

def regex2(request):
    return HttpResponse(f"abc로 시작");

def regex3(request):
    return HttpResponse(f"cba로 끝");

def regex4(request):
    return HttpResponse("*은 없거나 반복됨");

def regex5(request, txt):
    return HttpResponse(txt);
        
def regex6(request, txt):
    return HttpResponse(txt);

def regex7(request, txt):
    return HttpResponse(txt);

def regex8(request, txt):
    return HttpResponse(txt);

def regex9(request, txt):
    return HttpResponse(txt);

def regex10(request, txt):
    return HttpResponse(txt);

def phone(request, txt):
    return HttpResponse(txt);

def email(request, txt):
    return HttpResponse(txt);

def email1(request, txt):
    return HttpResponse(txt);