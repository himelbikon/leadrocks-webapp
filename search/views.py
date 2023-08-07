from django.shortcuts import render
from .models import LeadRocks


def index(request):
    data = {
        'leadrocks': LeadRocks.objects.all()
    }
    return render(request, 'search/index.html', data)
