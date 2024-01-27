from django.shortcuts import render, redirect

from . forms import CreateUserForm , LoginForm

from django.contrib.auth.decorators import login_required

# Authenticate models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login ,logout

# For contact_us Message and messagetags

from .models import Contact
from .models import CustomUser
from django.contrib import messages



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

        form = CreateUserForm(request.POST)

        if form.is_valid():

            user = form.save()
            user.birthday = request.POST.get('birthday')
            user.address = request.POST.get('address')  # Get the address from the form

            user.save()

            return redirect("my_login")
        else :
            messages.error(request,"Please fill all the details correctly.  Choosing a hard-to-guess, but easy-to-remember password is important!")


    context = {'registerform' :form}

    return render(request,'crm/registration.html',context=context)


def my_login(request):
    
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request,data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'loginform' :form} 

    return render(request,'crm/my_login.html',context=context)

def user_logout(request):

    auth.logout(request)

    return redirect("")




@login_required(login_url="my_login")
def dashboard(request):

    return render(request,'crm/dashboard.html')





