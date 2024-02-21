#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    print('blog')
    return HttpResponse('blog do app 1')


def exemplo(request):
    print('exemplo')
    return HttpResponse('exemplo do app 1')