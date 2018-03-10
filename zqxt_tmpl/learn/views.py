from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def strtel(request):
    string = u'zifu'
    return render(request,'zifu.html',{'string':string})

def listtel(request):
    TutoriaList = ['html','css','jave']
    return render(request,'list.html',{'TutoriaList':TutoriaList})

def dicttel(request):
    dict1 = {'site':'ziqiang','content':'jishu'}
    return render(request,'dict.html',{'dict1':dict1})
