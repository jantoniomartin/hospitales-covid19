from django.urls import path
from . import views


app_name = 'hospitals'
urlpatterns = [
    path('', views.RegionList.as_view(), name='region-list'),
    path('regions/<int:pk>/', views.RegionDetail.as_view(), name='region-detail'),
    path('hospital/<int:pk>/', views.HospitalDetail.as_view(), name='hospital-detail'),
    path('hospital/<int:pk>/add', views.HospitalAddNeed.as_view(), name='hospital-add-need'),
    path('need/<int:pk>/update', views.NeedUpdateView.as_view(), name='need-update'),
    path('resources/create', views.ResourceCreateView.as_view(), name='resource-create'),
    path('resources/<int:pk>/', views.ResourceDetail.as_view(), name='resource-detail'),
]

