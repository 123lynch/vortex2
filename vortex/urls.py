from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls', namespace='courses')),
    path('base/',include('base.urls', namespace='base')),
    path('blog/',include('blog.urls', namespace='blog')),
    path('account/', include('account.urls', namespace='account')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('basket/', include('basket.urls', namespace='basket')),
]