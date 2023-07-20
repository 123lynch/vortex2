from django.urls import path
from base import views
    
app_name = 'base'

urlpatterns = [
    path('contact/', views.Contact.as_view(),name="contact"),
    path('about/', views.About.as_view(),name="about")
]