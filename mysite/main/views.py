#coding = utf-8
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'main/index.html')
