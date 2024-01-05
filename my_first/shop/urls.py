from django.urls import path
from . import views

urlpatterns = [
    path('', views.page),
    path('contact', views.contact),

    path('about1/', views.about),
    path('viewproduct<int:myid>', views.viewproduct),
    path('checkout', views.checkout)            

]