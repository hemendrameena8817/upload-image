from django.urls import path,include
from image import views

urlpatterns = [
   
path('', views.home, name='image')

]
