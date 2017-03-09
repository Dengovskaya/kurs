from django.shortcuts import render
def Den(request):
    return render (request, 'Den.html')
def sales(request):
    return render (request, 'OMGU.html')
def news(request):
    return render (request, 'SIB.html')
