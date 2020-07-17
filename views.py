from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Entry


# Create your views here.
#def hello(request):
    #return render(request, 'hello.html')
class Indexview(TemplateView):
    model=Entry
    template_name = 'index.html'