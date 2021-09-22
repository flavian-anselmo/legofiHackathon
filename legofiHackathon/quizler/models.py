from django.db import models

class Student(models.Model):
    std_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
class Language(models.Model):
    c=models.BooleanField('C',default=False)
    cpp=models.BooleanField('C++',default=False)
    ruby=models.BooleanField('Ruby on Rails',default=False)
    perl=models.BooleanField('Perl',default=False)
    java=models.BooleanField('Java',default=False)
    asp=models.BooleanField('ASP',default=False) 
