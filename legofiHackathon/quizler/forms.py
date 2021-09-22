from django import forms
from django.forms import ModelForm
from quizler.models import*
class StudentForm(ModelForm):
    class Meta:
        model=Student
        #fecth the data from the student model 
        #take up all the fields 
        fields="__all__"
        
class LanguageForm(ModelForm):
    class Meta:
        model=Language
        #the fields will be check boxes 
        fields="__all__"        