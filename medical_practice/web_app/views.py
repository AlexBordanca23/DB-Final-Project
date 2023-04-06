from django.shortcuts import render, get_object_or_404,redirect
from .forms import DoctorForm,PatientContactForm, PatientDoctorsForm, PatientFinanceForm, PatientHealthForm, PatientVitalsForm, PatientIdForm
from .models import Doctors, PatientContact, PatientDoctors,PatientFinance, PatientHealth, PatientVitals, PatientId
from django.urls import reverse
from django.http import HttpResponseRedirect
from dal import autocomplete
# Create your views here.

def home(request):
    
    context = {}
    return render(request, 'index.html', context)

# Doctors views

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
    return render(request, "doctors_create_view.html", context)


def doctors_list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Doctors.objects.all()[:30]
         
    return render(request, "doctors_list_view.html", context)


def doctors_detail_view(request):
    
   if request.method == 'POST':
        # get the ID from the form data
        id = request.POST.get('id')
        # look up the model instance by ID
        instance = get_object_or_404(Doctors, doctor_id=id)
        return render(request, 'doctors_detail_view.html', {'data': instance})
   else:
        return render(request, 'doctors_detail_view.html')
    
def doctors_view_choices(request):
    
    context = {}
    return render(request,'doctors_view_choice.html',context)

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
        return render(request, 'doctors_update.html', {'form': form})
    
def doctors_delete_view(request, id):
    doctor = get_object_or_404(Doctors, doctor_id=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect(home)
    return render(request, 'doctors_delete.html', {'doctor': doctor})

# PatientContact views

def pc_create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = PatientContactForm(request.POST)
    if form.is_valid():
        form.save()
        
    form = PatientContactForm()     
    context['form']= form
    return render(request, "patient_contact_create_view.html", context)


def pc_list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = PatientContact.objects.all()[:30]
         
    return render(request, "patient_contact_list_view.html", context)


def pc_detail_view(request):
    
   if request.method == 'POST':
        # get the ID from the form data
        id = request.POST.get('id')
        # look up the model instance by ID
        instance = get_object_or_404(PatientContact, patient_id=id)
        return render(request, 'patient_contact_detail_view.html', {'data': instance})
   else:
        return render(request, 'patient_contact_detail_view.html')
    
def pc_view_choices(request):
    
    context = {}
    return render(request,'patient_contact_view_choice.html',context)

def pc_update_view(request, id):
    instance = get_object_or_404(PatientContact, patient_id=id)

    if request.method == 'POST':
        # update the model instance with the form data
        instance.name = request.POST.get('name')
        instance.save()
        return redirect(home)
    else:
        # prefill the form with the existing data
        form = PatientContactForm(instance=instance)
        return render(request, 'patient_contact_update.html', {'form': form})
    
def pc_delete_view(request, id):
    patient_contact = get_object_or_404(PatientContact, patient_id=id)
    if request.method == 'POST':
        patient_contact.delete()
        return redirect(home)
    return render(request, 'patient_contact_delete.html', {'patient_contact': patient_contact})

#PatientDoctors views

def pd_create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = PatientDoctorsForm(request.POST)
    if form.is_valid():
        form.save()
        
    form = PatientDoctorsForm()     
    context['form']= form
    return render(request, "patient_doctors_create_view.html", context)


def pd_list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = PatientDoctors.objects.all()[:30]
         
    return render(request, "patient_doctors_list_view.html", context)


def pd_detail_view(request):
    
   if request.method == 'POST':
        # get the ID from the form data
        id = request.POST.get('id')
        # look up the model instance by ID
        instance = get_object_or_404(PatientDoctors, patient_id=id)
        return render(request, 'patient_doctors_detail_view.html', {'data': instance})
   else:
        return render(request, 'patient_doctors_detail_view.html')
    
def pd_view_choices(request):
    
    context = {}
    return render(request,'patient_doctors_view_choice.html',context)

def pd_update_view(request, id):
    instance = get_object_or_404(PatientDoctors, patient_id=id)

    if request.method == 'POST':
        # update the model instance with the form data
        instance.name = request.POST.get('name')
        instance.save()
        return redirect(home)
    else:
        # prefill the form with the existing data
        form = DoctorForm(instance=instance)
        return render(request, 'patient_doctors_update.html', {'form': form})
    
def pd_delete_view(request, id):
    patient_doctors = get_object_or_404(PatientDoctors, patient_id=id)
    if request.method == 'POST':
        patient_doctors.delete()
        return redirect(home)
    return render(request, 'patient_doctors_delete.html', {'patient_doctors': patient_doctors})

# PatientFinance views

def pf_create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = PatientFinanceForm(request.POST)
    if form.is_valid():
        form.save()
        
    form = PatientFinanceForm()     
    context['form']= form
    return render(request, "patient_finance_create_view.html", context)


def pf_list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = PatientFinance.objects.all()[:30]
         
    return render(request, "patient_finance_list_view.html", context)


def pf_detail_view(request):
    
   if request.method == 'POST':
        # get the ID from the form data
        id = request.POST.get('id')
        # look up the model instance by ID
        interm = get_object_or_404(PatientId,pk =id)
        instance = get_object_or_404(PatientFinance, patient=interm)
        return render(request, 'patient_finance_detail_view.html', {'data': instance})
   else:
        return render(request, 'patient_finance_detail_view.html')
    
def pf_view_choices(request):
    
    context = {}
    return render(request,'patient_finance_view_choice.html',context)

def pf_update_view(request, id):
    instance = get_object_or_404(PatientFinance, patient=id)

    if request.method == 'POST':
        # update the model instance with the form data
        instance.name = request.POST.get('name')
        instance.save()
        return redirect(home)
    else:
        # prefill the form with the existing data
        form = PatientFinanceForm(instance=instance)
        return render(request, 'patient_finance_update.html', {'form': form})
    
def pf_delete_view(request, id):
    patient_finance = get_object_or_404(PatientFinance, patient=id)
    if request.method == 'POST':
        patient_finance.delete()
        return redirect(home)
    return render(request, 'patient_finance_delete.html', {'patient_finance': patient_finance})

#PatientHealth views

def ph_create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = PatientHealthForm(request.POST)
    if form.is_valid():
        form.save()
        
    form = PatientHealthForm()     
    context['form']= form
    return render(request, "patient_health_create_view.html", context)


def ph_list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = PatientHealth.objects.all()[:30]
         
    return render(request, "patient_health_list_view.html", context)


def ph_detail_view(request):
    
   if request.method == 'POST':
        # get the ID from the form data
        id = request.POST.get('id')
        # look up the model instance by ID
        interm = get_object_or_404(PatientId,pk =id)
        instance = get_object_or_404(PatientHealth, patient=interm)
        return render(request, 'patient_health_detail_view.html', {'data': instance})
   else:
        return render(request, 'patient_health_detail_view.html')
    
def ph_view_choices(request):
    
    context = {}
    return render(request,'patient_health_view_choice.html',context)

def ph_update_view(request, id):
    instance = get_object_or_404(PatientHealth, patient=id)

    if request.method == 'POST':
        # update the model instance with the form data
        instance.name = request.POST.get('name')
        instance.save()
        return redirect(home)
    else:
        # prefill the form with the existing data
        form = PatientHealthForm(instance=instance)
        return render(request, 'patient_health_update.html', {'form': form})
    
def ph_delete_view(request, id):
    patient_health = get_object_or_404(PatientHealth, patient=id)
    if request.method == 'POST':
        patient_health.delete()
        return redirect(home)
    return render(request, 'patient_health_delete.html', {'patient_health': patient_health})

# PatientVitals views

def pv_create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = PatientVitalsForm(request.POST)
    if form.is_valid():
        form.save()
        
    form = PatientVitalsForm()     
    context['form']= form
    return render(request, "patient_vitals_create_view.html", context)


def pv_list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = PatientVitals.objects.all()[:30]
         
    return render(request, "patient_vitals_list_view.html", context)


def pv_detail_view(request):
    
   if request.method == 'POST':
        # get the ID from the form data
        id = request.POST.get('id')
        # look up the model instance by ID
        interm = get_object_or_404(PatientId,pk=id)
        instance = get_object_or_404(PatientVitals, patient=interm)
        return render(request, 'patient_vitals_detail_view.html', {'data': instance})
   else:
        return render(request, 'patient_vitals_detail_view.html')
    
def pv_view_choices(request):
    
    context = {}
    return render(request,'patient_vitals_view_choice.html',context)

def pv_update_view(request, id):
    instance = get_object_or_404(PatientVitals, patient=id)

    if request.method == 'POST':
        # update the model instance with the form data
        instance.name = request.POST.get('name')
        instance.save()
        return redirect(home)
    else:
        # prefill the form with the existing data
        form = PatientVitalsForm(instance=instance)
        return render(request, 'patient_vitals_update.html', {'form': form})
    
def pv_delete_view(request, id):
    patient_vitals = get_object_or_404(PatientVitals, patient=id)
    if request.method == 'POST':
        patient_vitals.delete()
        return redirect(home)
    return render(request, 'patient_vitals_delete.html', {'patient_vitals': patient_vitals})

# PatientId views

def pid_create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = PatientIdForm(request.POST)
    if form.is_valid():
        form.save()
        
    form = PatientIdForm()     
    context['form']= form
    return render(request, "patient_id_create_view.html", context)


def pid_list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Doctors.objects.all()[:30]
         
    return render(request, "patient_id_list_view.html", context)


def pid_detail_view(request):
    
   if request.method == 'POST':
        # get the ID from the form data
        id = request.POST.get('id')
        # look up the model instance by ID
        instance = get_object_or_404(PatientId, patient_id=id)
        return render(request, 'patient_id_detail_view.html', {'data': instance})
   else:
        return render(request, 'patient_id_detail_view.html')
    
def pid_view_choices(request):
    
    context = {}
    return render(request,'patient_id_view_choice.html',context)

def pid_update_view(request, id):
    instance = get_object_or_404(PatientId, patient_id=id)

    if request.method == 'POST':
        # update the model instance with the form data
        instance.name = request.POST.get('name')
        instance.save()
        return redirect(home)
    else:
        # prefill the form with the existing data
        form = PatientIdForm(instance=instance)
        return render(request, 'patient_id_update.html', {'form': form})
    
def pid_delete_view(request, id):
    patient_id = get_object_or_404(PatientId, patient_id=id)
    if request.method == 'POST':
        patient_id.delete()
        return redirect(home)
    return render(request, 'patient_id_delete.html', {'patient_id': patient_id})


class PatientIdAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = PatientId.objects.all()

        if self.q:
            try:
                qs = qs.filter(patient_id=int(self.q))
            except ValueError:
                qs = qs.none()

        return qs