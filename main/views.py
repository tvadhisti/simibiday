from django.shortcuts import render

def show_main(request):
    context = {
        'title': 'ADMIN DASHBOARD',
    }

    return render(request, 'main.html', context)