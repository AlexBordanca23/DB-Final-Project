from django.shortcuts import render, get_object_or_404,redirect
from .forms import DoctorForm
from .models import Doctors
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    
    context = {}
    return render(request, 'index.html', context)

def doctors_create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = DoctorForm(request.POST)
    if form.is_valid():
        form.save()
        
    form = DoctorForm()     
    context['form']= form
    return render(request, "create_view.html", context)


def doctors_list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Doctors.objects.all()[:30]
         
    return render(request, "list_view.html", context)


def doctors_detail_view(request):
    
   if request.method == 'POST':
        # get the ID from the form data
        id = request.POST.get('id')
        # look up the model instance by ID
        instance = get_object_or_404(Doctors, doctor_id=id)
        return render(request, 'detail_view.html', {'data': instance})
   else:
        return render(request, 'detail_view.html')
    
def doctors_view_choices(request):
    
    context = {}
    return render(request,'view_choice.html',context)

def doctors_update_view(request, id):
    instance = get_object_or_404(Doctors, doctor_id=id)

    if request.method == 'POST':
        # update the model instance with the form data
        instance.name = request.POST.get('name')
        instance.save()
        return redirect(home)
    else:
        # prefill the form with the existing data
        form = DoctorForm(instance=instance)
        return render(request, 'update.html', {'form': form})
    
def doctors_delete_view(request, id):
    doctor = get_object_or_404(Doctors, doctor_id=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect(home)
    return render(request, 'delete.html', {'doctor': doctor})