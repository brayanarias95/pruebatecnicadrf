from rest_framework import routers
from app.API import appViewSet

router = routers.DefaultRouter()

router.register('api/tabla', appViewSet, 'tabla')

urlpatterns = router.urls