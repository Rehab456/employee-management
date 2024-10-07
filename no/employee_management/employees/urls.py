from django.urls import path
from .views import employee_list, add_employee, delete_employee

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('add/', add_employee, name='add_employee'),
    path('delete/<int:pk>/', delete_employee, name='delete_employee'),
]
