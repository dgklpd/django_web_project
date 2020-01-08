#coding = utf-8
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'mcshenzhous/index.html')
#index

#navbar_drop_down
def intro1(request):
    return render(request, 'intro/intro1.html')
def intro2(request):
    return render(request, 'intro/intro2.html')
def intro3(request):
    return render(request, 'intro/intro3.html')
#inters
def op1(request):
    return render(request, 'op/op1.html')
def op2(request):
    return render(request, 'op/op2.html')
def op3(request):
    return render(request, 'op/op3.html')
def op4(request):
    return render(request, 'op/op4.html')
def op5(request):
    return render(request, 'op/op5.html')
def op6(request):
    return render(request, 'op/op6.html')
def op7(request):
    return render(request, 'op/op7.html')
def op8(request):
    return render(request, 'op/op8.html')
def op9(request):
    return render(request, 'op/op9.html')
def op10(request):
    return render(request, 'op/op10.html')
def op11(request):
    return render(request, 'op/op11.html')





