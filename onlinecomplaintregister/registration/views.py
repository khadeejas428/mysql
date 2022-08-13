from hashlib import sha256
from django.shortcuts import render, redirect
from django.http   import HttpResponse
from .models import complaint_reg, reg_user

# Create your views here.
def register(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        password= sha256(pass2.encode()).hexdigest()
        reg_user(username=username,email=email,phone_no=phone_no,password=password).save()
        return redirect('login')  
    return render(request,'signup.html')
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        password2=sha256(password.encode()).hexdigest()
        user=reg_user.objects.filter(username=username,password=password2)
        if user:
            user_details=reg_user.objects.get(username=username,password=password2)
            id=user_details.id
            username_user=user_details.username
            request.session['id']=id
            request.session['username']=username_user
            return redirect('home')
    return render(request,'login.html')
def home(request):
        #id=request.session['id']
        #username=request.session['username']

        if request.method =='POST':
             name=request.POST.get('name')
             email=request.POST.get('email')
             message=request.POST.get('message')
             complaint_reg(name=name,email=email,message=message).save()
        return render(request,'home.html')
