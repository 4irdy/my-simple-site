from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

    # Note CRUD URLs
    path('notes/', views.note_list, name='note-list'),
    path('notes/new/', views.note_create, name='note-create'),
    path('notes/<int:pk>/edit/', views.note_update, name='note-update'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note-delete'),
]
