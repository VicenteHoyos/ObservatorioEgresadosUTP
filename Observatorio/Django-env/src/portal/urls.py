from django.urls import include, path

from portal import views

urlpatterns = [
    path('',views.inicio, name='inicio'),    
    path('contact',views.contacto, name='contact'),    
    path('about',views.about, name='about'),    
    path('invite',views.invitacionAdmin, name='inviteadmin'),      

]