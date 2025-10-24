{% comment %} 


- **User model** handling via Django’s `User` model  
- **Registration**: creating a new user  
- **Login**: authenticating and logging in a user  
- **Validation & redirection**  
- **Messages** for success/error feedback  

---

## ✅ Step-by-Step Backend Setup

---

### 🔧 1. **Update `views.py`**

In `user_auth/views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    return render(request, 'login.html')

def registration_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('registration')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect('registration')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')

    return render(request, 'registration.html')
```

---

### 🌐 2. **Update `urls.py`**

In `user_auth/urls.py`, link to the new views:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    # other paths...
]
```

---

### 📄 3. **Add CSRF Token & Form Action to Templates**

Update your `login.html` and `registration.html` (frontend files you already made) like this:

#### `login.html`:

```html
<form method="POST" action="{% url 'login' %}">
  {% csrf_token %}
  <!-- your login form fields -->
</form>
```

#### `registration.html`:

```html
<form method="POST" action="{% url 'registration' %}">
  {% csrf_token %}
  <!-- your registration form fields -->
</form>
```

Also, add this in both HTML files to show messages:

```html
{% if messages %}
  <ul class="messages">
    {% for message in messages %}
      <li class="{{ message.tags }}">{{ message }}</li>
    {% endfor %}
  </ul>
{% endif %}
```

---

### ✅ 4. **Make Sure Auth is in Installed Apps**

In your `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django.contrib.auth',
    'django.contrib.messages',
]
```

Also add `context_processors` for messages if not already:

```python
'django.contrib.messages.context_processors.messages',
```

---

### 💡 5. (Optional) Add Logout View

```python
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
```

And in `urls.py`:

```python
path('logout/', views.logout_view, name='logout'),
```

---

Let me know if you'd like:
- Password reset system
- Email verification
- Social login (like Google)
- Dashboard for logged-in users

Would you like me to help integrate this with your **Eventify** styling too?

{% endcomment %}