from django.urls import path
from apps.user.views import login, register, logout

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
]