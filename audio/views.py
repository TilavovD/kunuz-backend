# Create your views here.
from rest_framework.generics import ListAPIView

from .models import Audio
from .serializer import AudioListSerializer


class AudioListView(ListAPIView):
    serializer_class = AudioListSerializer
    queryset = Audio.objects.all()

