from django.shortcuts import render
from .forms import UserProfileInfoForm, UserFormInfo

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'appTwo/index.html',context_dict)

@login_required
def special(request):
    return HttpResponse("Logged in! Nice")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('appTwo:index'))

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('appTwo:index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Invalid login attempt")
            print("username : {} and password : {}".format(username,password))
            return HttpResponse("invalid login attempt")
    else:
        return render(request, 'appTwo/login.html',{})


def users(request):

    # form = NewUserForm()
    

    registered = False

    if request.method == 'POST':
        # form = NewUserForm(request.POST)
        user_form = UserFormInfo(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserFormInfo()
        profile_form = UserProfileInfoForm()

    return render(request, 'appTwo/users.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered
                            })
    # return render(request,'appTwo/users.html',{'form':form})

