from django.urls import path
from . import views

urlpatterns = [
    path("", views.employee_list, name='employee_list'),
    path("add/", views.add_employee, name='add_employee'),
    path("view/<int:id>/", views.employee_detail, name='employee_detail'),
    path("update/<int:id>/", views.update_employee, name='update_employee'),
    path("delete/<int:id>/", views.delete_employee, name='delete_employee'),
    path("hard_delete/<int:id>/", views.hard_delete_employee, name='hard_delete_employee'),
    path("restore/<int:id>/", views.restore_employee, name='restore_employee'),
    path("inactive/", views.inactive_employees, name='inactive_employees')
]