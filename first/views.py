from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from first import models


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, "Password doesn't match")
            return redirect('home')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account succesfully created , Now you can login")
        return redirect('home')
    else:
        return HttpResponse("404 - Not found")


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername , password=loginpass)
        if user is not None :
            login(request, user)
            messages.success(request, "successfully logged in")
            return redirect('about')
            
        else :
            messages.error(request, "Username Or Password is wrong" , extra_tags='danger')
            return redirect('home')
            
    else:
        return HttpResponse("404 - Not found")


def handlelogout(request):
    logout(request)
    messages.success(request, "loggout successfully")
    return redirect('home')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        ins = models.Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
    return render(request, 'contact.html')
    

def searchalgo(request):
    return render(request, 'searchalgo.html')

def sortalgo(request):
    return render(request, 'sortalgo.html')

def visualizer(request):
    return render(request, 'visualizer.html')


def quize(request):
    return render(request, 'quize.html')

def queue(request):
    return render(request, 'queue.html')
    
def stack(request):
    return render(request, 'stack.html')