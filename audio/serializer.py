from rest_framework.serializers import ModelSerializer

from .models import Audio


class AudioListSerializer(ModelSerializer):
    class Meta:
        model = Audio
        fields = ('title', "track", "image", "created_at")


