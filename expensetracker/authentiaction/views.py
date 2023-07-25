from django.shortcuts import render,redirect
from django.views import View
import json
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        context = {
            'fieldValues': request.POST
        }
        
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'authentication/register.html', context)
                
                # Create the user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful!')
                
        
        messages.error(request, 'Username or email already exists')
        return render(request, 'authentication/register.html', context)



class UsernameValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        username=data['username']
        if str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric character'},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'sorry username already exist'},status=400)
        return JsonResponse({'username_valid':True})



class LoginView(View):
    def get(self,request):
        return render(request,'authentication/login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' +
                                     user.username)
                    return redirect('index')
                messages.error(
                    request, 'Account is not active,please check your email')
                return render(request, 'authentication/login.html')
            messages.error(
                request, 'Invalid credentials,try again')
            return render(request, 'authentication/login.html')

        messages.error(
            request, 'Please fill all fields')
        return render(request, 'authentication/login.html')
    

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')