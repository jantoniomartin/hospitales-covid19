from django.urls import path
from . import views


app_name = 'makers'
urlpatterns = [
    path('', views.RegionList.as_view(), name='region-list'),
    path('regions/<int:pk>/', views.RegionDetail.as_view(), name='region-detail'),
    path('maker/<int:pk>/', views.MakerDetail.as_view(), name='maker-detail'),
]
