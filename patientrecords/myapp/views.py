from django.shortcuts import render

# Create your views here.
def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username == 'admin' and password == 'root':
            return redirect('homepage')  # Redirect to the homepage or desired page
    
    return render(request, 'loginpage.html', {})


def home_page(request):
    return render(request,'homepage.html',{})

from django.shortcuts import render, redirect
from .models import Patient

def register_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        gender = request.POST['gender']
        age = request.POST['age']
        dob = request.POST['dob']
        weight = request.POST['weight']
        phone = request.POST['phone']
        email = request.POST['email']
        
        
        patient = Patient(
            name=name, address=address, gender=gender, age=age,
            dob=dob, weight=weight, phone=phone, email=email
        )
        patient.save()
        
        return redirect('homepage')  # Redirect to the homepage or desired page
        
    return render(request, 'register_patient.html',{})


def consult_patient(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'consult_patient.html', context)

def view_patient(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)

    if request.method == 'POST':
        prescription = request.POST['prescription']
        observation = request.POST['observation']
        
        patient.prescription = prescription
        patient.observation = observation
        patient.save()
    
    context = {'patient': patient}
    return render(request, 'view_patient.html', context)


def consult_page(request):
    
    return render(request, 'consult_patient.html')


