from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Testfn(request):
    return HttpResponse('hlooooo')
def html1(request):
    return render(request,'login page.html')
 
