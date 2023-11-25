from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePageView.as_view(),name='index'),
    path('contact/',ContacView.as_view(),name='contact'),
    
    path('error/',ErrorView.as_view(),name='404'),
    path('pasrest/',PasresertView.as_view(),name='password-reset'),
    
    path('soat/',SoatView.as_view(),name='soat'),

    
]


# bu yerda htmllar ortasida otish uchun maxsus domen manzillar berilgan 