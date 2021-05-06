from django.urls import path 
from app.views import index, contact, ParticipantsCreateView, PaperCreateView

urlpatterns = [
    path('', index, name="index"),
    path('contact/add', contact, name="contact-add"),
    path('paper/add/', PaperCreateView, name="paper-add"),

    path('participants/add/', ParticipantsCreateView, name="participants-add"),
]