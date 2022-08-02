from django.db.models import F
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import News
from news.serializer import NewsListSerializer, NewsDetailSerializer


class MainNewsView(ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.filter(is_main=True)


class MostReadNewsView(ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.order_by("-views_count")


class LatestNewsView(ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.order_by("-created_at")


class RecommendedNewsView(ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.filter(is_recommended=True)


class GlobalNewsView(ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.filter(is_global=True)


class InquiryNewsView(ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.filter(is_inquiry=True)


class ArticleNewsView(ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.filter(is_article=True)


class AdvertisementsView(ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.filter(is_ad=True)


class NewsDetailView(RetrieveAPIView):
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        news = News.objects.filter(slug=self.kwargs['slug'])
        # news[0].views_count = F("views_count") + 1
        # news[0].save(update_fields=['views_count'])
        # print(news[0].views_count)

        return news
