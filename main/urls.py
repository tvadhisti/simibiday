from django.urls import path
from main.views import show_main, pickup_schedule, crud_menu

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('pickup-schedule', pickup_schedule, name='pickup_schedule'),
    path('crud-menu', crud_menu, name='crud_menu'),
]