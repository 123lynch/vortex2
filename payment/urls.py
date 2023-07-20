from django.urls import path
from payment import views

app_name='payment'

urlpatterns = [
    path('', views.BasketView, name='basket'),
    # path('orderplaced/', views.order_placed, name='order_placed'),
    # path('webhook/', views.stripe_webhook),
]