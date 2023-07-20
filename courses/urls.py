from django.urls import path

from courses import views

app_name = 'courses'

urlpatterns = [
    path('', views.course ,name="index"),
    path('courses/', views.course_display, name='courses'),
    path('<slug:slug>/', views.course_detail, name='course_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]