from django.http.response import HttpResponseRedirect
from app.models import Employee
from django.shortcuts import redirect, render
from .forms import EmployeeForm
# Create your views here.
def Register(request):

    context = {}
    if request.method == 'POST':
        context = EmployeeForm(request.POST)
        if context.is_valid():
            context.save()
            context = EmployeeForm()

    emp = Employee.objects.all()
    return render(request, 'app/register.html', {'form': context, 'employee': emp})

def Delete(request, id):
    if request.method == 'POST':
        data_delete = Employee.objects.get(pk=id)
        data_delete.delete()
        return HttpResponseRedirect('/')

def Update(request, id):
    if request.method == 'POST':
        pi = Employee.objects.get(pk=id)
        obj = EmployeeForm(request.POST, instance= pi)
        if obj.is_valid():
            obj.save()
    else:
        pi = Employee.objects.get(pk=id)
        obj = EmployeeForm(instance= pi)
    return render(request, 'app/update.html', {'form': obj})