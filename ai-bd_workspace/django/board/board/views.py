from django.http import HttpResponse

def chartMain(req):
    return HttpResponse("차트 페이지 입니다");

def chartWeekly(req, num):
    if 1<=int(num)<=52:
        return HttpResponse(f"{num} 주 차트 페이지 입니다");
    else:
        return HttpResponse(f"{num} 주 차트 페이지는 없습니다");

def chartMonth(req, num):
    if 1<=int(num)<=12:
        return HttpResponse(f"{num} 월 차트 페이지 입니다");
    else:
        return HttpResponse(f"{num} 월 차트 페이지는 없습니다");

def chartYear(rea, num):
    return HttpResponse(f"{num} 년 차트 페이지 입니다");