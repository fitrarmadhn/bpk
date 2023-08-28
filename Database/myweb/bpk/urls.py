from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='DATABASE'),
    path('byyy/',views.freelancer, name='freelancer'),
    path('ytrtt/',views.about, name='about'),
    path('bgdgd',views.job, name='job'),
]
