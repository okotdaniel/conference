from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from app.models import Participants, CommiteeMembers, Papers,Inquiries,Contacts,Program
# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def InquiryCreateView(request):
    return render(request, 'app/contact.html')


def ParticipantsCreateView(request):
    return render(request, 'app/participants_add.html')


def PaperCreateView(request):
    return render(request, 'app/paper_form.html')
    
 
# class based views 
class InquiryCreateView(CreateView):
    model = Inquiries
    fields = ['names','subject','message']
    success_url = '/'


class PaperCreateView(CreateView):
    model = Papers
    fields = ['title','author','fieldofstudy','company','profession']
    success_url = '/'


'''

class ParticipantsCreateView(CreateView):
    model = Inquiries
    fields = '__all__'
    fields = ['names','subject','message',]
    success_url = '/'


'''
