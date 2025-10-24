from django.contrib import admin
from django.urls import path
from user_auth import views

urlpatterns = [
    # path('',views.index,name='index'),
    # path('login/',views.login,name='login'),
    # path('registration/',views.registration,name='registration'),
    path('',views.home,name='home'),
    path("about/",views.about,name='about'),
    path('services/',views.services,name='services'),
    path('categories/',views.categories,name='categories'),
    path('contact/',views.contact,name='contact'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]