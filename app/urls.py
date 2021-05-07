from django.urls import path 
from app.views import index, InquiryCreateView, ParticipantsCreateView, PaperCreateView

urlpatterns = [
    path('', index, name="index"),
    #path('contact/add', InquiryCreateView, name="contact-add"),
    path('participants/add/', ParticipantsCreateView, name="participants-add"),
    #path('paper/add/', PaperCreateView, name="paper-add"),
    path('add/paper/', PaperCreateView.as_view(), name="paper-add"),

    path('add/inquiry/', InquiryCreateView.as_view(), name="inquiry-add")
    

]


'''

path('add/', ParticipantsCreateView.as_view(), name="create-view"),
path('add/', InqueryCreateView.as_view(), name="create-view"),

'''
