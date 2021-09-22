from django.shortcuts import redirect, render
from django.urls import reverse

def index(request):
    greeting='Welcome to Quizler'
    context={
		'msg':greeting
	  }
    return render(request,'index.html',context)

def register(request):
  #move the user to the registration form 
  reg='register'
  context={
    'reg':reg
  }
  return render(request,'register.html',context)
  