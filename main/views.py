from django.shortcuts import render


def crud_menu(request):
    context = {
        'title': 'MENU',
    }
    return render(request, 'crudMenu.html', context)

def room(request):
    context = {
        'title': 'ROOM',
    }
    return render(request, 'room.html', context)

def sclass(request):
    context = {
        'title': 'CLASS',
    }
    return render(request, 'class.html', context)

def child_in_class(request):
    context = {
        'title': 'CHILDREN IN CLASS',
    }
    return render(request, 'childInclass.html', context)

def daily_report(request):
    context = {
        'title': '[CHILD NAME]’s DAILY REPORT',
    }
    return render(request, 'dailyReport.html', context)

def daily_report_form(request):
    context = {
        'title': 'DAILY REPORT FORM',
    }
    return render(request, 'dailyReportForm.html', context)

def admin_dashboard(request):
    context = {
        'title': 'ADMIN DASHBOARD',
    }
    return render(request, 'adminDashboard.html', context)

def room_form(request):
    context = {
        'title': 'ROOM FORM',
    }
    return render(request, 'roomForm.html', context)

def menu_form(request):
    context = {
        'title': 'MENU FORM',
    }
    return render(request, 'menuForm.html', context)

def update_menu(request):
    context = {
        'title': 'UPDATE [MENU NAME] MENU',
    }
    return render(request, 'updateMenu.html', context)