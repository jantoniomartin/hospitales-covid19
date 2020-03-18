from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'hospitals'
urlpatterns = [
    path('regions/', views.RegionList.as_view()),
    path('regions/<int:pk>/', views.RegionDetail.as_view(), name='region-detail'),
    path('regions/<int:pk>/hospitals/', views.HospitalList.as_view()),
    path('hospitals/<int:pk>/', views.HospitalDetail.as_view(), name='hospital-detail'),
    path('resources/', views.ResourceList.as_view()),
    path('resources/<int:pk>/', views.ResourceDetail.as_view(), name='resource-detail'),
    path('needs/', views.NeedList.as_view()),
    path('needs/<int:pk>/', views.NeedDetail.as_view(), name='need-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
