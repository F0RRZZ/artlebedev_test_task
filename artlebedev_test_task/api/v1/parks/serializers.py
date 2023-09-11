from rest_framework.serializers import ModelSerializer

from parks.models import Park


class ParkSerializer(ModelSerializer):
    class Meta:
        model = Park
        fields = '__all__'
