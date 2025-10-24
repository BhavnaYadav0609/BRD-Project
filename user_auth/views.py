from django.shortcuts import render,HttpResponse

# Create your views here.
# def login(request):
#     return render(request, 'login.html')
# def registration(request):
#     return render(request, 'registration.html')
def index(request):
    return HttpResponse("hello lucifer")
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def categories(request):
    return render(request, 'categories.html')
def contact(request):
    return render(request, 'contact.html')
# views.py
# from django.shortcuts import render, redirect
# from .models import UserProfile
# from django.contrib import messages

# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']

#         if UserProfile.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists.")
#             return redirect('register')
        
#         if UserProfile.objects.filter(email=email).exists():
#             messages.error(request, "Email already registered.")
#             return redirect('register')

#         user = UserProfile(username=username, email=email, password=password)
#         user.save()
#         messages.success(request, "Registration successful!")
#         return redirect('login')

#     return render(request, 'registration.html')


# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         try:
#             user = UserProfile.objects.get(email=email, password=password)
#             request.session['user_id'] = user.id
#             messages.success(request, "Login successful!")
#             return redirect('home')
#         except UserProfile.DoesNotExist:
#             messages.error(request, "Invalid credentials")
#             return redirect('login')

#     return render(request, 'login.html')

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')
    
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # or your dashboard
            else:
                messages.error(request, "Invalid credentials.")
        except User.DoesNotExist:
            messages.error(request, "Email not found.")
    
    return render(request, 'login.html')
