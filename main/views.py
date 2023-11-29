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
def login(request):
    context = {
        'title': 'SIMIBIDAY - GROUP CODE',
    }
    return render(request, 'login.html', context)

def login_form(request):
    context = {
        'title': 'LOGIN FORM',
    }
    return render(request, 'loginForm.html', context)

def register(request):
    context = {
        'title': 'REGISTER',
    }
    return render(request, 'register.html', context)

def child_register(request):
    context = {
        'title': 'CHILD REGISTRATION FORM',
    }
    return render(request, 'childRegist.html', context)

def admin_register(request):
    context = {
        'title': 'ADMIN REGISTRATION FORM',
    }
    return render(request, 'adminRegist.html', context)


def caregiver_register(request):
    context = {
        'title': 'CAREGIVER REGISTRATION FORM',
    }
    return render(request, 'caregiverRegist.html', context)

def driver_register(request):
    context = {
        'title': 'DRIVER REGISTRATION FORM',
    }
    return render(request, 'driverRegist.html', context)

def user_dashboard(request):
    context = {
        'title': 'User Dashboard: [User’s Full Name]',
    }
    return render(request, 'userDashboard.html', context)

def child_program(request):
    context = {
        'title': 'CHILD PROGRAM DATA',
    }
    return render(request, 'childProgramExt.html', context)

def admin_activity(request):
    context = {
        'title': 'ACTIVITY',
    }
    return render(request, 'adminActivity.html', context)

def crd_program(request):
    context = {
        'title': 'MANAGE EXTRACURRICULAR',
    }
    return render(request, 'crdProgramExt.html', context)

def driver_pickup(request):
    context = {
        'title': 'PICKUP SCHEDULE',
    }
    return render(request, 'driverPickupSchedule.html', context)

def edit_activity(request):
    context = {
        'title': 'ACTIVITY FORM',
    }
    return render(request, 'editActivity.html', context)

def child_list(request):
    context = {
        'title' : 'Child List',
    }
    return render(request, 'childList.html', context)

def admin_offered_program(request):
    context = {
        'title' : 'Admin Offered Program',
    }
    return render(request, 'adminOfferedProgram.html', context)

def manage_ext(request):
    context = {
        'title' : 'Manage Extracuricular',
    }
    return render(request, 'manageExt.html', context)

def update_activity(request):
    context = {
        'title' : 'Update [Activity Name] Activity',
    }
    return render(request, 'updateActivity.html', context)
def payment_history_admin(request):
    context = {
        'title' : 'Payment History',
    }
    return render(request, 'paymentHistoryAdmin.html', context)

def payment_history_child(request):
    context = {
        'title' : 'Payment History',
    }
    return render(request, 'paymentHistoryChild.html', context)

def payment_form(request):
    context = {
        'title' : 'Payment Form',
    }
    return render(request, 'paymentForm.html', context)

def crud_extracurricular(request):
    context = {
        'title' : 'Extracurricular',
    }
    return render(request, 'crudExtracurricular.html', context)

def extracurricular_detail(request):
    context = {
        'title' : 'Extracurricular Detail',
    }
    return render(request, 'extracurricularDetail.html', context)

def extracurricular_form(request):
    context = {
        'title' : 'Extracurricular Form',
    }
    return render(request, 'extracurricularForm.html', context)

def update_extracurricular(request):
    context = {
        'title' : 'Update Extracurricular',
    }
    return render(request, 'updateExtracurricular.html', context)
