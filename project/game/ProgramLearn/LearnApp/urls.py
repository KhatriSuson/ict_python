from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('level/<int:level_id>/', views.challenges, name='challenges'),
    path('challenge/<int:challenge_id>/', views.challenge_detail, name='challenge_detail'),
]