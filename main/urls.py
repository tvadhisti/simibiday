from django.urls import path

from . import views 
from uuid import UUID

urlpatterns = [
    path('admin-offered-program', views.admin_offered_program, name='admin_offered_program'),
    path('delete_program/<uuid:id>/', views.delete_program, name='delete_program'),
    path('crud-menu', views.crud_menu, name='crud_menu'),
    path('menu-form', views.menu_form, name='menu_form'),
    path('update-menu/<uuid:pk>', views.update_menu, name='update_menu'),
    path('delete-menu/<uuid:id>/', views.delete_menu, name='delete_menu'),
    path('room', views.room, name='room'),
    path('room-form', views.room_form, name='room_form'),
    path('delete_room/<int:room_id>/', views.delete_room, name='delete_room'),
    path('admin-dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('crud-extracurricular', views.crud_extracurricular, name='crud_extracurricular'),
    path('extracurricular-form', views.extracurricular_form, name='extracurricular_form'),
    path('extracurricular-detail/<uuid:pk>', views.extracurricular_detail, name='extracurricular_detail'),
    path('update-extracurricular/<uuid:pk>', views.update_extracurricular, name='update_extracurricular'),
    path('delete-extracurricular/<uuid:id>/', views.delete_extracurricular, name='delete_extracurricular'),
    path('child-list', views.child_list, name='child_list'),
    path('class', views.sclass, name='class'),
    path('child-in-class', views.child_in_class, name='child_in_class'),
    path('daily-report', views.daily_report, name='daily_report'),
    path('daily-report-form', views.daily_report_form, name='daily_report_form'),
    path('', views.login, name='login'),
    path('login-form', views.login_form, name='login_form'),
    path('register', views.register, name='register'),
    path('child-register', views.child_register, name='child_register'),
    path('admin-register', views.admin_register, name='admin_register'),
    path('caregiver-register', views.caregiver_register, name='caregiver_register'),
    path('driver-register', views.driver_register, name='driver_register'),
    path('user-dashboard', views.user_dashboard, name='user_dashboard'),
    path('child-program', views.child_program, name='child_program'),
    path('admin-activity', views.admin_activity, name='admin_activity'),
    path('crd-program', views.crd_program, name='crd_program'),
    path('driver-pickup', views.driver_pickup, name='driver_pickup'),
    path('edit-activity', views.edit_activity, name='edit_activity'),

    path('payment-history-admin', views.payment_history_admin, name='payment_history_admin'),
    path('payment-history-child', views.payment_history_child, name='payment_history_child'),
    path('payment-form', views.payment_form, name='payment_form'),
=======
]