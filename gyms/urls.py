from rest_framework.routers import DefaultRouter
from .views import GymViewSet, MembershipViewSet

router = DefaultRouter()
router.register('gyms', GymViewSet)
router.register('memberships', MembershipViewSet)

urlpatterns = router.urls