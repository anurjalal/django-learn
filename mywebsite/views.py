from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'judul': "Kelas terbuka",
        'kontributor': "faqihza",
    }
    return render(request, 'index.html', context)