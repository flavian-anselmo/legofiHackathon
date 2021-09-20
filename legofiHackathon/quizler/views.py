from django.shortcuts import render
def index(request):
    greeting='helloe'
    context={
		'msg':greeting
	}
    return render(request,'index.html',context)

