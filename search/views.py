from django.shortcuts import render
from .models import LeadRocks


def index(request):
    data = {
        'leadrocks': LeadRocks.objects.all()
    }
    return render(request, 'search/index.html', data)


def query(request):
    d = request.GET

    # query_data = set()
    leadrocks = None

    # ===================================
    full_name = d.get('full_name')
    if full_name:
        if not leadrocks:
            leadrocks = LeadRocks.objects.filter(
                full_name__icontains=full_name)
        else:
            leadrocks = leadrocks.filter(full_name__icontains=full_name)

    # ===================================
    first_name = d.get('first_name')
    if first_name:
        if not leadrocks:
            leadrocks = LeadRocks.objects.filter(
                first_name__icontains=first_name)
        else:
            leadrocks = leadrocks.filter(first_name__icontains=first_name)

    # ===================================
    last_name = d.get('last_name')
    if last_name:
        if not leadrocks:
            leadrocks = LeadRocks.objects.filter(
                last_name__icontains=last_name)
        else:
            leadrocks = leadrocks.filter(last_name__icontains=last_name)

    # ===================================
    job_title = d.get('job_title')
    if job_title:
        if not leadrocks:
            leadrocks = LeadRocks.objects.filter(
                job_title__icontains=job_title)
        else:
            leadrocks = leadrocks.filter(job_title__icontains=job_title)

    data = {
        'leadrocks': leadrocks
    }
    return render(request, 'search/query.html', data)
