from django.shortcuts import render,redirect
from .import forms
from hospitalapp.models import Appointment,Administration,Donation
from .forms import appointmentform,donationform
# Create your views here.
def index(request):
    return render(request,'index.html')

# def myview(request):
#     form=forms.management()
#     if request.method=='POST':
#         form=forms.management(request.POST)
#         if form.is_valid():
#             print('form is valid')
#             print('last name',form.cleaned_data['lastname'])
#             # selected_option = form.cleaned_data['dropdown']
#     return render(request,'index.html',{'myform':form})

    # dropdown_options = ['Dermatology', 'Orthopedic', 'Neurology']  # Replace this with your data
    # context = {'dropdown_options': dropdown_options}
    # return render(request, 'index.html', {'form':selected_option})

def registrationview(request):
    form=forms.userregistrationform()
    if request.method=='POST':
        form=forms.userregistrationform(request.POST)
        if form.is_valid():
            print('form is valid')
    return render(request,'index.html',{'myform':form})

def appointment(request):
    appoint=Appointment.objects.all()
    return render(request,'appointment.html',{'appointment':appoint})
def addpatient(request):
    if request.method=='POST':
        form=appointmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=appointmentform()
    return render(request,'addpatient.html',{'form':form})

def specialities(request):
    return render(request,'specialities.html')

def donation(request):
    if request.method=='POST':
        form=donationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=donationform()
    return render(request,'bloodcompaign.html',{'donationform':form})

def myadmin(request):
    return render(request,'myadmin.html')
def doctorappointments(request):
    appointments=Appointment.objects.all()
    return render(request,'appointmentlist.html',{'appointments':appointments})

def myadmin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        print(email," ",password)
        administration=Administration.objects.filter(email=email,password=password)
        if administration.exists():
            print('hello')
            request.session["email"]=email
            return render(request,'myadmin.html',{'msg':email})
        else:
            return render(request, "administration_login.html", {"msg": "email or password not exist"})
    return render(request, "administration_login.html", {"msg": ""})

def blooddoners(request):
    doners=Donation.objects.all()
    return render(request,'blooddonation.html',{'doners':doners})

def management(request):
    return render(request,'management.html')