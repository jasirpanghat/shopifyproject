
from datetime import timedelta, timezone
import datetime
import random
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from django.db.models import Q

from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login,logout as authlogout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache,cache_control
from django.core.mail import send_mail
from shopifyproject.settings import EMAIL_HOST_USER
from django.core.validators import EmailValidator

# Create your views here.

def user_login(request):
    

   

    
    

    return render(request,'userlogin.html')
def user_signup(request):
    
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        number=request.POST.get('number')
        email=request.POST.get('email')
        if not all([ username, email, password]):
                messages.error(request,'Please fill up all the fields.')
                return redirect('login')
        elif CustomUser.objects.filter(username=username).exists():
            
                messages.error(request, 'The username is already taken')
                return redirect('login')
        if not username:
                messages.error(request, 'Please provide a username')
                return redirect('login')
        elif not username.strip():
                messages.error(request, 'The username is not valid')
                return redirect('login')
        if not all([username, email, password]):
                messages.error(request,'please fill up all the fields.')
                return redirect('login')
        elif CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'The username is already taken')
                return redirect('login')
        
        elif len(password) < 6:
                messages.error(request, 'The password should be at least 6 characters')
                return redirect('login')
       
        elif not any(char.isupper() for char in password):
                messages.error(request, 'Password must contain at least one uppercase letter')
                return redirect('login')
        elif not any(char.islower() for char in password):  # Corrected condition
                messages.error(request, 'Password must contain at least one lowercase letter')
                return redirect('login')
        elif not any(char.isdigit() for char in password):
                messages.error(request, 'Password must contain at least one digit')
                return redirect('login')
        elif not re.match(r"^[\w\.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email): 
                messages.error(request, 'Please enter a valid email address')
                return redirect('login')
        elif not EmailValidator(email):
                messages.error(request, 'Enter a valid email')
                return redirect('login')
        elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'This email is already registered')
                return redirect('login')

        generate_otp_and_send_email(email)
        if username:
            # CustomUser.objects.create_user(username=username, password=password,phone=number,email=email)
            pass

            # c=CustomUser.objects.all()
            # print(c)
        else:
            print('hi')
    return render(request,'userlogin.html')

def user_signup(request):
       return render(request,'usersignup.html')

def user_home(request):

    return render(request,'index.html')


def generate_otp_and_send_email(request,email):
    otp = random.randint(1000, 9999)
    otp_generated_at = timezone.now().isoformat()

    request.session['otp'] = {' otp': otp, 'otp_generated_at': otp_generated_at}

    send_mail(
        subject='Welcome',
        message=f'Your OTP for verification is: {otp}',
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=True
    )

def otp(request):
        if request.method == 'POST':
               
                otp1 = request.POST.get('otp1')
                otp2 = request.POST.get('otp2')
                otp3 = request.POST.get('otp3')
                otp4 = request.POST.get('otp4')

                full_otp = otp1 + otp2 + otp3 + otp4
                if 'otp' in request.session:
                        otp_data= request.session['otp']
                        otp=otp_data['otp']
                        otp_generated=otp_data['otp_generated_at']
                
    
    
                        if datetime.now() <=  otp_generated +timedelta(minutes=5) :
                                # Compare OTPs
                                if full_otp == otp:
                                # OTP is correct and not expired
                                # Proceed with further actions (e.g., user authentication)
                                        return HttpResponse("OTP verification successful!")
                                else:
                                        return HttpResponse("Incorrect OTP! Please try again.")
                        else:
                                return HttpResponse("OTP has expired. Please request a new one.")
                else:
                        return HttpResponse("OTP verification session data not found.")
        else:
                return render(request,'otp.html')
        


        

      