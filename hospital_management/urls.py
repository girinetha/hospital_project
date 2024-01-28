"""
URL configuration for hospital_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospitalapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    # path('',views.myview),
    path('',views.registrationview),
    path('appointment/',views.appointment),
    path('addpatient/',views.addpatient,name='addpatient'),
    path('specialities/',views.specialities,name='specialities'),
    path('bloodcompaign/',views.donation,name='donation'),
    path('myadmin/',views.myadmin,name='myadmin'),
    path('appointments/',views.doctorappointments,name='doctorappointments'),
    # path('administration/',views.adminlogin,name='adminlogin'),
    path('blooddonation/',views.blooddoners,name='blooddoners'),
    path('management/',views.management,name='management')
]
