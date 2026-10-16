from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:pk>/edit/', views.edit_message, name='edit_message'),
    path('messages/<int:pk>/delete/', views.delete_message, name='delete_message'),
    path('messages/<int:pk>/restore/', views.restore_message, name='restore_message'),
]
