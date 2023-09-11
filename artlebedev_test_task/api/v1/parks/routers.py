from rest_framework.routers import DefaultRouter

from api.v1.parks.views import ParkViewSet

router = DefaultRouter()
router.register(
    r'parks',
    ParkViewSet,
    basename='parks',
)
