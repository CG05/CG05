from django.shortcuts import render
from phonebook.models import PhoneBook
# Create your views here.
def index(req):
    # 이름, 전화번호
    alluser = PhoneBook.objects.values("id", "이름", "전화번호");
    content = {
        "alluser" : alluser,
    }
    return render(req, 'phonebook/index.html', content);

def phoneAdd(req):

    return render(req, 'phonebook/add.html');

def phoneDelete(req):

    return render(req, 'phonebook/delete.html');

def phoneDetail(req, userId):
    userInfo = PhoneBook.objects.values("이름", "전화번호", "이메일", "주소", "생년월일").get(id=userId)
    print(userInfo)
    alluser = PhoneBook.objects.values("id", "이름", "전화번호");
    content = {
        "userInfo" : userInfo,
        "alluser" : alluser
    }

    return render(req, 'phonebook/detail.html', content);

def phoneUpdate(req):

    return render(req, 'phonebook/update.html');