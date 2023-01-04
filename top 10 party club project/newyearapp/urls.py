from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('details',views.details,name='details'),
    path('maps',views.maps,name='maps'),
    path('details',views.details,name='details'),
    path('wheel',views.wheel,name='wheel'),

    path('logout',views.logout,name="logout"),
    path('login',views.login.as_view(),name='login'),
    path('b_login',views.b_login.as_view(),name='b_login'),
    path('register',views.register.as_view(),name='register'),

    path('sales',views.sales,name='sales'),

    path('booking',views.booking.as_view(),name='booking'),
    path('payment',views.payment.as_view(),name='payment'),
    path('chat',views.chat,name="chat"),
    
]