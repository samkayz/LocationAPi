from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as dj_login, logout as s_logout
from django.contrib.auth import user_logged_in
from django.dispatch.dispatcher import receiver
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.utils.html import strip_tags
from django.db.models import Sum
from location.settings import EMAIL_FROM
from .models import *
import random
import string
import uuid
import datetime
import json
import math
from django.http import HttpResponse
from datetime import datetime
UserModel = get_user_model()



def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if UserModel.objects.filter(email=email, is_superuser=1).exists():
            messages.error(request, "Invalid Credentials")
            return redirect('signin')
        else:

            user = authenticate(email=email, password=password)

            if user is not None:
                dj_login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid Credentials")
                return redirect('signin')
    else:
        return render(request, 'signin.html')


def signup(request):
    api_key = uuid.uuid4().hex[:20].lower()
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
                return redirect('signup')
            elif UserModel.objects.filter(phone=phone).exists():
                messages.error(request, "Mobile Number Taken")
                return redirect('signup')
            else:
                user = UserModel.objects.create_user(
                    username=email,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    api_key=api_key,
                    date_registered=now
                )
                user.save()
                messages.success(request, "Registration Successfull")
                return redirect('signin')
    else:
        return render(request, 'signup.html')


@login_required(login_url='signin')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='signin')
def profile(request):
    return render(request, 'profile.html')


def logout(request):
    s_logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('signin')