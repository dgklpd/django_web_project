#coding = utf-8
from django.shortcuts import render, get_object_or_404

# Create your views here.
def a1(request):
    return render(request, 'articles/a1.html')
