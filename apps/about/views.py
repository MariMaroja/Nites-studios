from django.shortcuts import render, get_object_or_404, redirect
from apps.about.models import AboutUs
from apps.about.forms import AboutUsForms
from django.contrib import messages

def about_us():
    us = AboutUs.objects.filter(posted=True)
    return render('about/about.html', {"cards": us})

def about(request, us_id):
    us = get_object_or_404(AboutUs, pk=us_id)
    return render(request, 'about/about.html', {"us": us})


def new_about(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User not logged')
        return redirect('login')
    
    form = AboutUsForms
    if request.method == 'POST':
        form = AboutUsForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New About Us!')
            return redirect ('about_us')

    return render(request, 'gallery/newus.html', {'form':form})

def edit_about(request, us_id):
    us = AboutUs.objects.get(id=us_id)
    form = AboutUsForms(instance=us)

    if request.method == 'POST':
        form = AboutUsForms(request.POST, request.FILES, instance=us)
        if form.is_valid():
            form.save()
            messages.success(request, 'About Us Edited!')
            return redirect('about_us')
        
def delete_about(request, us_id):
    us = AboutUs.objects.get(id=us_id)
    us.delete()
    messages.success(request, 'About Us Successfully Deleted!')
    return redirect('about_us')