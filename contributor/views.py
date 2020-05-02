from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login as dj_login, logout as s_logout
from django.contrib.auth.decorators import login_required, permission_required
from user.models import *
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Sum
from location.settings import EMAIL_FROM
import uuid
import re
import csv
import io
from django.http import HttpResponse
from datetime import datetime
UserModel = get_user_model()


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if UserModel.objects.filter(email=email, is_superuser=1).exists():
            users = authenticate(email=email, password=password)

            if users is not None:
                dj_login(request, users)
                return redirect('dashboard')
            else:
                messages.error(request, 'Access Denied!!')
                return redirect('/contributor/login')
        else:
            messages.error(request, 'Please Only Contributor can Login here')
            return redirect('/contributor/login')
    else:
        return render(request, 'contributor/signin.html')



def c_signup(request):
    base_date_time = datetime.now()
    now = (datetime.strftime(base_date_time, "%Y-%m-%d %H:%M"))
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if UserModel.objects.filter(email=email).exists():
                messages.error(request, "Email Taken")
                return redirect('c_signup')
            elif UserModel.objects.filter(phone=phone).exists():
                messages.error(request, "Mobile Number Taken")
                return redirect('c_signup')
            else:
                user = UserModel.objects.create_user(
                    username=email,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    is_superuser = "1",
                    phone=phone,
                    date_registered=now
                )
                user.save()
                messages.success(request, "Registration Successfull")
                return redirect('/contributor/login')
    else:
        return render(request, 'contributor/signup.html')



@permission_required('is_superuser', login_url='/contributor/login')
def dashboard(request):
    return render(request, 'contributor/home.html')


def logout(request):
    s_logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('/contributor/login')


@permission_required('is_superuser', login_url='/contributor/login')
def profile(request):
    return render(request, 'profile.html')
