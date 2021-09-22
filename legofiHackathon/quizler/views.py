from django.shortcuts import redirect, render
from django.urls import reverse
from quizler.forms import*

def index(request):
    greeting='Welcome to Quizler'
    context={
		'msg':greeting
	  }
    return render(request,'index.html',context)

def register(request):
  #move the user to the registration form 
  context={}
  form_student =StudentForm(request.POST)
  form_language=LanguageForm(request.POST)
  
  if request.method == 'GET':
    context['student']=form_student
    context['language']=form_language
    return render(request,'register.html',context)
  elif request.method=='POST':
    if form_student.is_valid() and form_language.is_valid():
      #if both the forms are valid save the data 
      form_language.save()
      form_student.save()
      return render(request,'confirm.html',context)
  