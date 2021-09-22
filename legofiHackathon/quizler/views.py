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
  form =StudentForm(request.POST)
  if request.method == 'GET':
    context['form']=form
    return render(request,'register.html',context)
  elif request.method=='POST':
    if form.is_valid():
      form.save()
      return render(request,'confirm.html',context)
  