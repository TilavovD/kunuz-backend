from django.urls import path

from .views import AudioListView

urlpatterns = [
    path("list/", AudioListView.as_view(), name="audio_list"),


    ]
