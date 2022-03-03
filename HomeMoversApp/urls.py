from django.urls import path
from django.urls import include
from . import views

app_name = "HomeMoversApp"

urlpatterns = [
    # path('', views.root, name="root"),
    path('', views.home, name="homepage"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('news/', views.news, name="news")
]