from django.shortcuts import render

def index(request):
    return render(request,'personal/home.html')

def contact(request):
    return render(request,'personal/basic.html', {'content':['If you wanna contact me mail Me : ','abc@gmail.com']})
