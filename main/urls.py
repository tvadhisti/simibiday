from django.urls import path
from main.views import crud_menu, room, sclass, child_in_class, daily_report, daily_report_form, admin_dashboard, room_form, menu_form, update_menu, login, login_form, register, child_register,admin_register, caregiver_register, driver_register, user_dashboard, admin_activity,child_program, crd_program, driver_pickup,edit_activity
from main.views import crud_menu, room, sclass, child_in_class, daily_report, daily_report_form, admin_dashboard, room_form, menu_form, update_menu, login, login_form, register, child_register,admin_register, caregiver_register, driver_register, user_dashboard, child_list, admin_offered_program,manage_ext, update_activity, payment_history_admin, payment_history_child, payment_form,crud_extracurricular, extracurricular_detail, extracurricular_form, update_extracurricular, admin_create_offered_program, offered_program_details, add_new_activity, add_new_menu, child_daily_report

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
    path('child-program', child_program, name='child_program'),
    path('admin-activity', admin_activity, name='admin_activity'),
    path('crd-program', crd_program, name='crd_program'),
    path('driver-pickup', driver_pickup, name='driver_pickup'),
    path('edit-activity', edit_activity, name='edit_activity'),
    path('child-list', child_list, name='child_list'),
    path('admin-offered-program', admin_offered_program, name='admin_offered_program'),
    path('manage-ext', manage_ext, name='manage_ext'),
    path('update-act', update_activity, name='update_activity'),
    path('payment-history-admin', payment_history_admin, name='payment_history_admin'),
    path('payment-history-child', payment_history_child, name='payment_history_child'),
    path('payment-form', payment_form, name='payment_form'),
    path('crud-extracurricular', crud_extracurricular, name='crud_extracurricular'),
    path('extracurricular-detail', extracurricular_detail, name='extracurricular_detail'),
    path('extracurricular-form', extracurricular_form, name='extracurricular_form'),
    path('update-extracurricular', update_extracurricular, name='update_extracurricular'),
    path('admin-create-offered-program', admin_create_offered_program, name='admin_create_offered_program'),
    path('offered-program-details', offered_program_details, name='offered_program_details'),
    path('add-new-activity', add_new_activity, name='add_new_activity'),
    path('add-new-menu', add_new_menu, name='add_new_menu'),
    path('child-daily-report', child_daily_report, name='child_daily_report')
]