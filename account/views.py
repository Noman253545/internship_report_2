from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def signupPage(request):
        
        if request.method=='POST':
         
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')
         
            if pass1!=pass2:

                return HttpResponse("Your password and conform password are not same!!!")
         
            else:

                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
        
            return redirect('login_page')
            #  return HttpResponse("User has been created successfully!!!")
                        
        return render(request, 'signup.html')


def login_page(request):
    if request.method=='POST':
        username=request.Post.get('username')
        pass1=request.Post.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('work_submission')
        else:
            return HttpResponse("Username or Passwordis incorrect!!!")

    return render(request, 'login.html')


        