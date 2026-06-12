from django.urls import path
from apps.about.views import *

urlpatterns = [
    path('about-us', about_us, name='about_us'),
    path('about', about, name='about'),
    path('new-about', new_about, name='new_about'),
    path('edit-about', edit_about, name='edit_about'),
    path('delete-about', delete_about, name='delete_about')
]