from rest_framework.routers import DefaultRouter
from .views import TestView

router = DefaultRouter()
router.register('test', TestView)

urlpatterns = router.urls