from django.urls import path
from myapp import views

urlpatterns = [

             path('login', views.log_in, name='login'),
             path('homepage',views.home_page, name= 'homepage'),
             path('register', views.register_patient, name='register_patient'),
             path('consult', views.consult_patient, name='consult_patient'),
        
             path('consult/view/<int:patient_id>/', views.view_patient, name='view_patient'),

             path('consult_p', views.consult_page, name='consult_page'),

            path('', views.log_in, name='log'),  # Adding the root path


             
]
         
