from django.urls import path
from apps.employee.views import identity, new_identity, delete_identity

urlpatterns = [
    path('id', identity, name='identity'),
    path('new-id', new_identity, name='new_identity'),
    path('delete-id', delete_identity, name='delete_identity')
]