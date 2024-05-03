from django.shortcuts import render,redirect
from studentapp.models import register

# Create your views here.

def home(request):
    return render(request,'home.html')

def read(request):
    data=register.objects.all()
    return render(request,'read.html',{'values':data})

def editpage(request,pk):
    data=register.objects.get(id=pk)
    return render(request,'edit.html',{'data':data})


def insert(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phonenumber=request.POST.get('phonenumber')
        email=request.POST.get('email')
        course=request.POST.get('course')
        address=request.POST.get('address')

        register.objects.create(first_name=first_name,last_name=last_name,phonenumber=phonenumber,email=email,course=course,address=address)
        return redirect('read')
    
def edit(request,pk):
    if request.method=='POST':
        data=register.objects.get(id=pk)
        data.first_name=request.POST.get('first_name')
        data.last_name=request.POST.get('last_name')
        data.phonenumber=request.POST.get('phonenumber')
        data.email=request.POST.get('email')
        data.course=request.POST.get('course')
        data.address=request.POST.get('address')
        data.save()
        return redirect('read')
    
def Delete(request,id):
    value=register.objects.get(id=id)
    value.delete()
    return redirect('read')





