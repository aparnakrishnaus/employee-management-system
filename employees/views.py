from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages
# Create your views here.

#fetch employee
def employee_list(request):
    employees = Employee.objects.filter(status = 'ACTIVE')

    selected_department = request.GET.get('department')
    if selected_department and selected_department != "All":
        employees = employees.filter(department=selected_department)

    departments  = Employee.objects.values_list('department', flat=True).distinct()

    return render(request, 'employees/employee_list.html',{
        'employees' : employees,
        'departments' : departments,
        'selected_department' : selected_department or "All"
    })

#add
def add_employee(request):
    if request.method == 'POST':
       form = EmployeeForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, "Employee added successfully!")
           return redirect('employee_list')
       
    else:
        form = EmployeeForm()
    
    return render(request, 'employees/employee_form.html',{
        'form' : form
    })
 

#fetch by id
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employees/employee_detail.html',{
        'employee' : employee
    })


#update
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
       form = EmployeeForm(request.POST, instance=employee)

       if form.is_valid():
          if form.has_changed():
            form.save()
            messages.success(request, "Employee details updated successfully!")

          else:
              messages.info(request, "No changes made to the employee.")
          return redirect('employee_list')
    
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/employee_form.html',{
        'form' : form
    })

    
#soft delete
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.status = 'INACTIVE'
    employee.save()
    messages.warning(request, f"{employee.name} marked as INACTIVE.")
    return redirect('employee_list')


#trash
def inactive_employees(request):
    employees = Employee.objects.filter(status='INACTIVE')
    return render(request, 'employees/inactive_list.html',{
        'employees' : employees
    })

#restore
def restore_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.status = 'ACTIVE'
    employee.save()
    messages.success(request, f"{employee.name} restored successfully.")
    return redirect('inactive_employees')


#hard delete
def hard_delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    messages.error(request, f"{employee.name} permanently deleted.")
    return redirect('inactive_employees')




