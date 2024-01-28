from django.shortcuts import render, redirect
 
from . forms import CreateUserForm , LoginForm,AuthenticationForm

from django.contrib.auth.decorators import login_required

# Authenticate models and functions

from django.contrib.auth.models import auth,User
from .models import CustomUser
from django.contrib.auth import authenticate, login ,logout

# For contact_us Message and messagetags

from .models import Contact
from .models import CustomUser
from django.contrib import messages

# Email

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from elevate.settings import EMAIL_HOST_USER
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 


def homepage(request):
 
    return render(request,'crm/index.html')

def about_us(request):
 
    return render(request,'crm/about_us.html')

def contact_us(request):

    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        print(first_name, last_name, email , phone, message)


        if len(first_name)<2 or len(last_name)<2 or len(email)<5 or len(phone)<10 or len(message)<4:
            messages.error(request,"Please fill the form correctly ")
        else:
            
            contact = Contact(first_name=first_name,last_name=last_name,email=email,phone=phone,message=message)
            contact.save()
            messages.success(request,"Thank you for your response")
        
    return render(request,'crm/contact_us.html')

def registration(request):

    form = CreateUserForm()

    if request.method == 'POST':

        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # birthday = request.POST.get('birthday')
        # address = request.POST.get('address')


        form = CreateUserForm(request.POST)

        if form.is_valid():

            otp = random.randint(100000,999999)
            send_mail("User data: ",f"Verify your email by otp: \n{otp}",EMAIL_HOST_USER,[email],fail_silently=True)

            return render(request,'crm/verify.html',{'otp':otp,'first_name':first_name,'last_name':last_name,'username':username,'email':email,'password1':password1,'password2':password2})
        else :
            messages.error(request,"Please fill all the details correctly.  Choosing a hard-to-guess, but easy-to-remember password is important!")


    context = {'registerform' :form}

    return render(request,'crm/registration.html',context=context)

@csrf_exempt
def verify(request):

    if request.method == "POST":
        userotp = request.POST.get('otp')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # birthday = request.POST.get('birthday')
        # address = request.POST.get('address')

        if(password1 == password2):
            
            hashed_password = make_password(password1)
            form = User(first_name=first_name,last_name=last_name,username=username,email=email,password=hashed_password)
            form.save()

        print("OTP",userotp)
    return JsonResponse({'data': 'Hello'}, status=200)


def my_login(request):
    
    form = LoginForm()
    if request.method == 'POST':

        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:

                login(request, user)
                return redirect("dashboard")

    context = {'loginform' :form} 

    return render(request,'crm/my_login.html',context=context)

def user_logout(request):

    auth.logout(request)

    return redirect("")




@login_required(login_url="my_login")
def dashboard(request):

    return render(request,'crm/dashboard.html')





