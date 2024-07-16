from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from .views import FetchUsersView,save_appointment

STATIC_URL = '/static/'

urlpatterns = [

    # for testing
    path('test', views.test,name='test'),
    path('test1', views.test1,name='test1'),
    path('apptest', views.apptest,name='apptest'),
    path('tabletest', views.tabletest,name='tabletest'),
    path('add_patient/', views.add_patient, name='add-patient'),
    path('fetch-users/', FetchUsersView.as_view(), name='fetch_users'),
    path('save_appointment/', save_appointment, name='save_appointment'),
    path('delete_appointment/', views.delete_appointment, name='delete_appointment'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('get_medicine_data/', views.get_medicine_data, name='get_medicine_data'),


    path('dashboard', views.Dashboard,name='dashboard'),
    path('appointments', views.Appointments,name='appointments'),
    path('patientdashboard', views.Patientdashboard,name='patientdashboard'),
    path('appointmentlist', views.Appointmentlist,name='appointmentlist'),
    path('doctorappointment', views.Doctorappointment,name='doctorappointment'),

    # event
    path('get_events/', views.get_events, name='get_events'),
    # path('events_add/', views.add_event, name='add_event'), 
    path('add_event/', views.add_event, name='add_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('update_event/<int:event_id>/', views.update_event, name='update_event'),

    # add patient
    path('submit_patient',views.SubmitPatientForm,name='submit_patient'),
    path('fetch_patient_data/', views.fetch_patient_data, name='fetch_patient_data'),
    path('edit_patient/<int:patient_id>/', views.edit_patient, name='edit_patient'),

    path('login', views.Login,name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    path('patient-data/', views.patient_data, name='patient_data'),
    path('patient-count-per-day/', views.patient_count_per_day, name='patient_count_per_day'),
    path('patient/<int:patient_id>/', views.get_patient_details, name='get_patient_details'),

    # add medicine
    path('save-data/', views.save_data, name='save_data'),
    path('delete-data/', views.delete_data, name='delete_data'),
    path('delete-medicine/', views.delete_medicine, name='delete_medicine'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
