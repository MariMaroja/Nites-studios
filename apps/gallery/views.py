from django.shortcuts import render, get_object_or_404, redirect
from apps.gallery.models import Characters, Videos, Synopsis
from apps.gallery.forms import CharactersForms, VideosForms, SynopsisForms
from django.contrib import messages

def index():
    character = Characters.objects.filter(published=True)
    video = Videos.objects.filter(posted=True)
    synopsis = Synopsis.objects.filter(reveal=True)
    content = character, video, synopsis
    return render('gallery/index.html', {"cards": content})

def employee(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User not logged')
        return redirect('login') 
    
    character = Characters.objects.filter(published=True)
    video = Videos.objects.filter(posted=True)
    synopsis = Synopsis.objects.filter(reveal=True)
    content = character, video, synopsis   
    return render('gallery/employee.html', {"cards": content})

def persona(request, chara_id):
    character = get_object_or_404(Characters, pk=chara_id)
    return render(request, 'gallery/character.html', {"character": character})

def record(request, video_id):
    video = get_object_or_404(Videos, pk=video_id)
    return render(request, 'gallery/video.html', {"video": video})

def summary(request, synopsis_id):
    synopsis = get_object_or_404(Synopsis, pk=synopsis_id)
    return render(request, 'gallery/synopsis.html', {"synopsis": synopsis})

def search(request):
    character = Characters.objects.filter(published=True)
    video = Videos.objects.filter(posted=True)
    synopsis = Synopsis.objects.filter(reveal=True)
    content = character, video, synopsis

    if "search" in request.GET:
        search_content = request.GET['search']
        if search_content:
            character = character.filter(content__icontanins=search_content) | video = video.filter(content__icontanins=search_content) | synopsis = synopsis.filter(content__icontanins=search_content)

    return render(request, "gallery/index.html", {"cards": content})

def new_character(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User not logged')
        return redirect('login')
    
    form = CharactersForms
    if request.method == 'POST':
        form = CharactersForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New character posted!')
            return redirect('index')
        
    return render(request, 'gallery/new_character.html', {'form':form})

def new_video(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User not logged')
        return redirect('login')
    
    form = VideosForms
    if request.method == 'POST':
        form = VideosForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New video posted!')
            return redirect('index')
        
    return render(request, 'gallery/new_video.html', {'form':form})

def new_synopsis(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User not logged')
        return redirect('login')
    
    form = SynopsisForms
    if request.method == 'POST':
        form = SynopsisForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New synopsis posted!')
            return redirect('index')
        
    return render(request, 'gallery/new_synopsis.html', {'form':form})

def edit_character(request, chara_id):
    characters = Characters.objects.get(id=chara_id)
    form = CharactersForms(instance=characters)

    if request.method == 'POST':
        form = CharactersForms(request.POST, request.FILES, instance=characters)
        if form.is_valid():
            form.save()
            messages.success(request, 'Character edited!')
            return redirect('index')
        
    return render(request, 'gallery/edit_character.html', {'form': form, 'chara_id': chara_id})

def edit_video(request, video_id):
    video = Videos.objects.get(id=video_id)
    form = VideosForms(instance=video)

    if request.method == 'POST':
        form = VideosForms(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video edited!')
            return redirect('index')
        
    return render(request, 'gallery/edit_video.html', {'form': form, 'video_id': video_id})

def edit_synopsis(request, synopsis_id):
    synopsis = Synopsis.objects.get(id=synopsis_id)
    form = SynopsisForms(instance=synopsis)

    if request.method == 'POST':
        form = SynopsisForms(request.POST, request.FILES, instance=synopsis)
        if form.is_valid():
            form.save()
            messages.success(request, 'Synopsis edited!')
            return redirect('index')
        
    return render(request, 'gallery/synopsis.html', {'form': form, 'synopsis_id': synopsis_id})

def delete_character(request, chara_id):
    character = Characters.objects.get(id=chara_id)
    character.delete()
    messages.success(request, 'Character deleted!')
    return redirect('index')

def delete_video(request, video_id):
    video = Videos.objects.get(id=video_id)
    video.delete()
    messages.success(request, 'Video deleted!')
    return redirect('index')

def delete_synopsis(request, synopsis_id):
    synopsis = Synopsis.objects.get(id=synopsis_id)
    synopsis.delete()
    messages.success(request, 'Synopsis deleted!')
    return redirect('index')

def filter(request, category, title, text):
    character = Characters.objects.filter(published=True, category=category)
    video = Videos.objects.filter(published=True, title=title)
    synopsis = Synopsis.objects.filter(published=True, text=text)

    content = character, video, synopsis

    return render(request, 'gallery/index.html', {"cards": content})