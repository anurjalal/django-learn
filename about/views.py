from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul' : 'Kelas Terbuka',
        'subjudul' : 'About',
        'nav' : [
            ['/' , "Home" ],
            ['/blog', "Blog"],
            ['/about', "About"]
        ],
        'banner' : 'about/img/banner_about.png'
    }
    return render(request, 'about/index.html', context)