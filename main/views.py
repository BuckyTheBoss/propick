from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contact
# Create your views here.


def homepage(request):
    return render(request, 'main/Home.html')


class ContactView(CreateView):
    template_name = 'main/Contact.html'
    model = Contact
    fields = '__all__'