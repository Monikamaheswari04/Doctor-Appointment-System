from django.shortcuts import render
from .models import Userdata
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request,method=['GET','POST']):
    if request.method=="POST":
       email=request.POST.get('email')
       password=request.POST.get('password')
       confirm_password=request.POST.get('confirm_password')

       user=Userdata.objects.filter(email=email)

       if user.exists():
           messages.info(request,"User is already exists")
       elif password !=confirm_password:
           messages.info(request,"Password does not match")
       else:
           Userdata.objects.create(email=email,password=password)
           return render(request,'login.html')

    return render(request,'signup.html')



def login(request,method=['GET','POST']):
    if request.method=="POST":
       email=request.POST.get('email')
       password=request.POST.get('password')
      

       user=Userdata.objects.filter(email=email,password=password)

       if user.exists():
           return render(request,'home.html')
       else:
           messages.error(request,'Email and Password are incorrect')
           
   

    return render(request,'login.html')
