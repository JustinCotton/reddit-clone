from .views import UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register('users', UserViewSet)
 
urlpatterns = router.urls