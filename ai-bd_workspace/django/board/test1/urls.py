from test1 import views
from django.urls import path, re_path, include

urlpatterns = [
    # path("chart/test1/", t1views.main),
    path("", views.main),
]

# url : chart/
# - 차트 페이지 입니다.
# url : chart/weekly/1~52
# - 1 주 차트 페이지 입니다
# - 52 주 차트 페이지 입니다
# - 53 주 차트 페이지는 없습니다

# url : chart/month/1~12
# - 1 월 차트 페이지 입니다
# - 12 월 차트 페이지 입니다
# - 13 월 차트 페이지는 없습니다
 
