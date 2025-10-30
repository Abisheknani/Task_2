from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Measurment

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == '1234':
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request,'login.html')

def index_view(request):
    if request.method =='POST':
        DISTANCE_1 = request.POST.get('DISTANCE_1')
        DISTANCE_2 = request.POST.get('DISTANCE_2')
        PAD_THICKNESS_1=request.POST.get('PAD_THICKNESS_1')
        PAD_THICKNESS_2=request.POST.get('PAD_THICKNESS_2')
        DISTANCE_3 = request.POST.get('DISTANCE_3')
        DISTANCE_4 = request.POST.get('DISTANCE_4')

        obj=Measurment()
        obj.DISTANCE_1=DISTANCE_1
        obj.DISTANCE_2=DISTANCE_2
        obj.PAD_THICKNESS_1=PAD_THICKNESS_1
        obj.PAD_THICKNESS_2=PAD_THICKNESS_2
        obj.DISTANCE_3=DISTANCE_3
        obj.DISTANCE_4=DISTANCE_4
        obj.save()
        mydata=Measurment.objects.last()
        return render(request, 'index.html',{"datas":mydata})
    
    return render(request, 'index.html')

# Create your views here.
