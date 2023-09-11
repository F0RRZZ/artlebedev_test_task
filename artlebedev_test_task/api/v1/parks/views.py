from rest_framework.viewsets import ModelViewSet

from api.permissions import IsAdminOrReadOnly
from api.v1.parks.serializers import ParkSerializer
from parks.models import Park


class ParkViewSet(ModelViewSet):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer
    permission_classes = (IsAdminOrReadOnly,)
