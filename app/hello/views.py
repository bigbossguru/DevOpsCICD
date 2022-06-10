from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'This project using a popular Python Django Framework'
    }
    return render(request, 'index.html', context)