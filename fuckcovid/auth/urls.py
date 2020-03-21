from django.urls import path
from . import views


app_name = 'auth'
urlpatterns = [
    path('profile/', views.ProfileDetail.as_view(), name='profile-detail'),
    path('profile/edit/', views.ProfileUpdate.as_view(), name='profile-update'),
]

