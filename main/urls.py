from django.urls import path
from main.views import crud_menu, room, sclass, child_in_class, daily_report, daily_report_form, admin_dashboard, room_form, menu_form, update_menu

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
]