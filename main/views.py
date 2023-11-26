from django.shortcuts import render

def admin_dashboard(request):
    context = {
        'title': 'ADMIN DASHBOARD',
    }

    return render(request, 'adminDashboard.html', context)

def pickup_schedule(request):
    context = {
        'title': 'PICKUP SCHEDULE',
    }
    return render(request, 'pickupSchedule.html', context)

def crud_menu(request):
    context = {
        'title': 'MENU',
    }
    return render(request, 'crudMenu.html', context)