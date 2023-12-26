from django.shortcuts import render, redirect, get_object_or_404
from .models import MENU, ROOM, PROGRAM, EXTRACURRICULAR, CHILD
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def child_list(request):
    context = {
        'title' : 'Child List',
    }
    return render(request, 'childList.html', context)

def admin_offered_program(request):
    programs = PROGRAM.objects.all().order_by('Name')
    context = {
        'title' : 'Admin Offered Program',
        'programs': programs
    }
    return render(request, 'adminOfferedProgram.html', context)

@require_POST
def delete_program(request, id):
    data = get_object_or_404(PROGRAM, ProgramID=id)
    data.delete()
    return JsonResponse({'message': 'Data deleted successfully'})

def crud_extracurricular(request):
    extraCurriculars = EXTRACURRICULAR.objects.all().order_by('Name')
    context = {
        'title' : 'Extracurricular',
        'extraCurriculars': extraCurriculars
    }
    return render(request, 'crudExtracurricular.html', context)

def extracurricular_form(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Day = request.POST['Day']
        Hour = request.POST['Hour']
        data = EXTRACURRICULAR(Name=Name, Day=Day, Hour=Hour)
        data.save()
        return redirect('crud_extracurricular')
    else:
        context = {
            'title' : 'Extracurricular Form',
        }
        return render(request, 'extracurricularForm.html', context)

def extracurricular_detail(request, pk):
    extraCurricular = EXTRACURRICULAR.objects.get(ExtracurricularID=pk)
    context = {
        'title' : 'Extracurricular Detail',
        'extraCurricular': extraCurricular
    }
    return render(request, 'extracurricularDetail.html', context)

def update_extracurricular(request, pk):
    extraCurricular = EXTRACURRICULAR.objects.get(ExtracurricularID=pk)
    if request.method == "POST":
        extraCurricular.Name = request.POST['Name']
        extraCurricular.Day = request.POST['Day']
        extraCurricular.Hour = request.POST['Hour']
        extraCurricular.save()
        return redirect('crud_extracurricular')
    else:
        context = {
            'title' : 'Update Extracurricular',
            'extraCurricular': extraCurricular
        }
        return render(request, 'updateExtracurricular.html', context)
@require_POST
def delete_extracurricular(request, id):
    data = get_object_or_404(EXTRACURRICULAR, ExtracurricularID=id)
    data.delete()
    return JsonResponse({'message': 'Data deleted successfully'})

def crud_menu(request):
    menus = MENU.objects.all().order_by('Name')
    context = {
        'title': 'MENU',
        'menus': menus
    }
    return render(request, 'crudMenu.html', context)

def menu_form(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Type = request.POST['Type']
        data = MENU(Name=Name, Type=Type)
        data.save()
        return redirect('crud_menu')
    else:
        context = {
            'title': 'MENU FORM',
        }
        return render(request, 'menuForm.html', context)

def update_menu(request,pk):
    menu = MENU.objects.get(ID=pk)
    if request.method == "POST":
        menu.Name = request.POST['Name']
        menu.Type = request.POST['Type']
        menu.save()
        return redirect('crud_menu')
    else:
        context = {
            'title': 'UPDATE {} MENU'.format(menu.Name),
            'menu': menu
        }
        return render(request, 'updateMenu.html', context)
@require_POST
def delete_menu(request, id):
    data = get_object_or_404(MENU, ID=id)
    data.delete()
    return JsonResponse({'message': 'Data deleted successfully'})

def room(request):
    rooms = ROOM.objects.all().order_by('RoomNo')
    context = {
        'title': 'ROOM',
        'rooms': rooms
    }
    return render(request, 'room.html', context)

def room_form(request):
    if request.method == "POST":
        RoomNo = request.POST['RoomNo']
        Area = request.POST['Area']
        data = ROOM(RoomNo=RoomNo, Area=Area)
        data.save()
        return redirect('room')
    else:
        context = {
            'title': 'ROOM FORM',
        }
        return render(request, 'roomForm.html', context)
    
@require_POST
def delete_room(request, room_id):
    room = get_object_or_404(ROOM, RoomNo=room_id)
    room.delete()
    return JsonResponse({'message': 'Room deleted successfully'})

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
        'title': '[CHILD Name]’s DAILY REPORT',
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
