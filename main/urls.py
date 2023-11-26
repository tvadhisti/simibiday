from django.urls import path
from main.views import crud_menu, room, sclass, child_in_class, daily_report, daily_report_form, admin_dashboard, room_form, menu_form, update_menu, login, login_form, register, child_register,admin_register, caregiver_register, driver_register, user_dashboard

app_name = 'main'

urlpatterns = [
    path('crud-menu', crud_menu, name='crud_menu'),
    path('room', room, name='room'),
    path('class', sclass, name='class'),
    path('child-in-class', child_in_class, name='child_in_class'),
    path('daily-report', daily_report, name='daily_report'),
    path('daily-report-form', daily_report_form, name='daily_report_form'),
    path('admin-dashboard', admin_dashboard, name='admin_dashboard'),
    path('room-form', room_form, name='room_form'),
    path('menu-form', menu_form, name='menu_form'),
    path('update-menu', update_menu, name='update_menu'),
    path('', login, name='login'),
    path('login-form', login_form, name='login_form'),
    path('register', register, name='register'),
    path('child-register', child_register, name='child_register'),
    path('admin-register', admin_register, name='admin_register'),
    path('caregiver-register', caregiver_register, name='caregiver_register'),
     path('driver-register', driver_register, name='driver_register'),
     path('user-dashboard', user_dashboard, name='user_dashboard'),
]