from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages



def home(request):
    return render(request, "dashboard.html")





def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return render(request, "dashboard.html")
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "index.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        
        email = request.POST['email']
        password = request.POST['password']
      
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        
        
        
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, password)
        # people=People.objects.
        
        
        myuser.is_active = True
        myuser.save()
       
        
        return redirect('signin')
        
        
    return render(request, "index.html")

