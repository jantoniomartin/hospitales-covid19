from rest_framework import routers

from .views import UserViewSet

app_name = 'auth'
router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls
