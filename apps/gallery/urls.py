from django.urls import path
from apps.gallery.views import index, persona, record, summary, search, new_character, new_synopsis, new_video, edit_character, edit_synopsis, edit_video, delete_character, delete_synopsis, delete_video, filter

urlpatterns = [
    path('', index, name='index'),
    path('character', persona, name='persona'),
    path('video', record, name='record'),
    path('synopsis', summary, name='summary'),
    path('search', search, name='search'),
    path('new-character', new_character, name='new_character'),
    path('new-video', new_video, name='new_video'),
    path('new-synopsis', new_synopsis, name='new_synopsis'),
    path('edit-character/<int:chara_id>', edit_character, name='edit_character'),
    path('edit-video/<int:video_id>', edit_video, name='edit_video'),
    path('edit-synopsis/<int:synopsis_id>', edit_synopsis, name='edit_synopsis'),
    path('delete-character/<int:chara_id>', delete_character, name='delete_character'),
    path('delete-video/<int:video_id>', delete_video, name='delete_video'),
    path('delete-synopsis/<int:synopsis_id>', delete_synopsis, name='delete_synopsis'),
    path('filter/<str:content>', filter, name='filter')
]