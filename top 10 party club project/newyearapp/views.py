from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import LoginForm,RegisterForm,BookingForm
from .models import ProductModel,BookingModel
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render (request,'index.html')

def details(request):
    return render (request,'details.html')    

def maps(request):
    return render (request,'maps.html')        

def wheel(request):
    return render (request,'wheel.html')        
     
class login(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            return redirect('login')

class b_login(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'b_login.html',{'form':form})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('wheel')
        else:
            return redirect('b_login')

def logout(request):
    auth_logout(request)
    return redirect('home')



class register(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'register.html',{'form':form})
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        User.objects.create_user(username=username,email=email,password=password)
        form.save()
        return redirect('login')


class booking(View):
    def get(self,request):
        form = BookingForm()
        messages.success(request,f"Congrats {request.user} !! Your Token has been Applied Successfully!!")
        return render(request,'booking.html',{'form':form})
        
    def post(self,request):
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            person = form.cleaned_data['person']
            msg = form.cleaned_data['msg']
            booking = BookingModel(name=name,email=email,phone=phone,person=person,msg=msg)
            booking.save()
        return redirect('payment')



def sales(request):
    products = ProductModel.objects.all()      
    return render(request,'sales.html',{'products':products})

class payment(View):
    def get(self,request):
        return render(request,'payment.html')
        
    def post(self,request):
        messages.success(request,f"Congratulations {request.user}, Your Payment Proceed Successfully !!")
        return redirect('payment')

def chat(request):
    return render(request,'chat.html')