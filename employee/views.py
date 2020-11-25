from django.shortcuts import render,HttpResponse,render,redirect
from .models import Employees

def home(request):
    return render(request,"empfirst.html")

def add(request):
    
   
    if request.method=="GET":
         return render(request,'empadd.html')
    else:
        prop=Employees()
        prop.EmployeeName=request.POST.get('ename')
        prop.Address=request.POST.get('address')
        prop.Phone=request.POST.get('phone')
        prop.Email=request.POST.get('email')
        
        prop.Image=request.FILES['img']
       
        
        prop.save()
        return redirect(vemp)

def vemp(request):
    vemp=Employees.objects.all()
    return render(request,'emppview.html',{'data': vemp})

