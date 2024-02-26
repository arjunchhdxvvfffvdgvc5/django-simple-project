from.import views
from django.urls import path
urlpatterns = [
    path('',views.index), 
    path('ab',views.contact),
    path('co',views.about),
    path('lg',views.login),
    path('rg',views.register)
]                                      
       