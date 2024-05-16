from django.db import models

# Create your models here.
# DB 연동 클래스
class PhoneBook(models.Model):
    이름 = models.CharField(max_length=50, null=False)
    전화번호 = models.CharField(max_length=15)
    이메일 = models.EmailField()
    주소 = models.CharField(max_length=100)
    생년월일 = models.DateField()

    def __str__(self) -> str:
        return self.이름