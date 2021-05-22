from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('mbti/', TypeIndicatorListView.as_view(), name='mbti'),
    path('mbti/<slug:slug>', TypeIndicatorDetailView.as_view(), name='detail'),
    path('test/', test, name='test'),
] 