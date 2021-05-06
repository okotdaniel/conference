from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'app/index.html')


def contact(request):
    return render(request, 'app/contact.html')


def ParticipantsCreateView(request):
    return render(request, 'app/participants_add.html')


def PaperCreateView(request):
    return render(request, 'app/paper_add.html')
    