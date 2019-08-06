from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import  User
from .models import form
from django.core.mail import send_mail

# Create your views here.
def register(request):
    if request.method == "POST":
        
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*']
        if password1 == password2:
            if len(password1) >= 8:
                for i in password1:
                    if i in specialCharacters:
                        userobj = form(name= name, email= email, password=password1)
                        userobj.save()
                        send_mail("Registration successfull", "Hi "+ name +", we have received your details and will process soon.", 'ram.myname@hushmail.com', [email])
                        return render(request, 'thanks.html', {'name': name})
                messages.info(request, 'Password Should have atleast one Special Character.')
                return redirect('register')
            else:
                messages.info(request, 'Password should be minimum 8 Characters')
                return redirect('register')
        else:
            messages.info(request, 'Password did not match...')
            return redirect('register')
    elif request.method == "GET":
        return render(request, 'index.html')

        
