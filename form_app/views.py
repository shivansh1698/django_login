from django.shortcuts import render
from form_app.models import UserInfo,UserTextData
from form_app.forms import UserForm,TextForm,ImageForm
from django.core import validators
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

#-----------------
#    HOME PAGE    
#-----------------

def index(request):
    logout(request)
    return render(request,'form_app/index.html')

#-----------------
#    SIGN-UP PAGE    
#-----------------

def form_sign(request):
    user_form = UserForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return render(request,'form_app/submit.html',{'status':'success_sign','user':user_form.cleaned_data['username']})
                    
    return render(request,'form_app/form_content.html',{'form':user_form})

#-----------------
#    LOG-IN PAGE    
#-----------------

def form_log(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,'form_app/submit.html',{'user':username,'status':'success_log'})

            else:
                return HttpResponse("account not active")
        
        else:
            print('login failed')
            print('username: {} and password: {}'.format(username,password))
            return HttpResponse("invalid login details")

    return render(request,'form_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request,'form_app/index.html')

def read_data(request):
    str = ""
    for obj in users.objects.all():
        str += obj.get_data('email') + "<br>"
    return HttpResponse(str)

@login_required
def save_text(request):
    user = request.user
    for obj in UserTextData.objects.all():
        if obj.get_data('user') == user:
            return HttpResponse("text data already saved")
    text = TextForm()
    if request.method=='POST':
        text = TextForm(request.POST)
        if text.is_valid():
            text.save()
            print("text saved successfully")
            return render(request,'form_app/submit_text.html')
        else:
            print(text.errors)
            return HttpResponse("invalid text details")
    
    return render(request,'form_app/text.html',{'text_form':text, })

@login_required
def image(request):
    image = ImageForm(request.POST,request.FILES)
    if request.method== 'POST':
        if image.is_valid():
            image.save()
            print("image saved successfully")

        else:
            return HttpResponse("invalid image")

    return render(request,'form_app/image.html',{'image_form':image})

def sample(request):
    return render(request,'form_app/relative_urls.html')

def test(request):
    return render(request,'form_app/test.html')

def success_save(request):
    return render(request,'form_app/submit_text.html')