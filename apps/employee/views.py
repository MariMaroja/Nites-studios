from django.shortcuts import render, get_object_or_404, redirect
from apps.employee.forms import IdentifyForms
from apps.employee.models import Identify
from django.contrib import messages

def identity(request, identity_id):
    identify = get_object_or_404(Identify, pk=identity_id)
    return render('employee/indentity.html', {"cards":identify})

def new_identity(request, identity_id):
    if not request.user.is_authenticated:
        messages.error(request, 'User not logged')
        return redirect('login')
    
    form = IdentifyForms
    if request.method == 'POST':
        form = IdentifyForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New id posted!')
            return redirect('index')
        
    return render(request, 'employee/new_identity.html', {'form': form})

def delete_identity(request, identity_id):
    identify = Identify.objects.get(id=identity_id)
    identify.delete()
    messages.success(request, 'Succesfully deleted!')
    return redirect('index')