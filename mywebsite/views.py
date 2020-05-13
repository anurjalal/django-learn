from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'judul': "Kelas terbuka",
        'subjudul': "selamat datang",
        'nav' : [
            ['/' , "Home" ],
            ['/blog', "Blog"],
            ['/about', "About"]
        ],
        'banner' : 'img/banner_home.png',
    }
    return render(request, 'index.html', context)