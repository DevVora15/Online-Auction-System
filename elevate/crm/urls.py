from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.homepage,name=''),

    path('about_us',views.about_us,name='about_us'),

    path('contact_us',views.contact_us,name='contact_us'),
    
    path('registration',views.registration,name='registration'),

    path('verify',views.verify,name='verify'),    

    path('my_login',views.my_login,name='my_login'),

    path('dashboard',views.dashboard,name='dashboard'),

    path('user_logout',views.user_logout, name='user_logout'),

]