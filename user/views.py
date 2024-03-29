from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth import logout
# Create your views here.


# index
def index(request):
    return render(request, 'user/index.html', {'title':'index'})


# refister here

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            role = form.cleaned_data.get('role')

            # email conformation
            # htmly = get_template('user/Email.html')
            # d = {'username':username}
            # subject, from_email, to = 'welcom', 'Abhishek2010112@akgec.ac.in', email
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()

            messages.success(request, f'Your account has been created ! You are now able to Login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html',{'form':form, 'titel':'register here'})
        

# Login forms
    
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # role = request.POST['role']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username}  !!')
            return redirect('index')
        else:
            messages.info(request, f'account does not exit please signin first')

    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})


# def logout(request):
#     logout(request)
#     return render(request, 'user/index.html')


    