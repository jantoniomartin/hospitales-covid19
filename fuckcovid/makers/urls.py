from django.urls import path
from . import views


app_name = 'makers'
urlpatterns = [
    path('', views.RegionList.as_view(), name='region-list'),
    path('regions/<int:pk>/', views.RegionDetail.as_view(), name='region-detail'),
    path('maker/<int:pk>/', views.MakerDetail.as_view(), name='maker-detail'),
    path('maker/create/', views.MakerCreate.as_view(), name='maker-create'),
    path('maker/<int:pk>/update/', views.MakerUpdate.as_view(), name='maker-update'),
    path('maker/<int:pk>/add/', views.ProductionCreate.as_view(), name='production-create'),
    path('production/<int:pk>/update', views.ProductionUpdate.as_view(), name='production-update'),
]
