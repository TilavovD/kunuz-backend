from django.urls import path

from news.views import \
    MainNewsView, \
    MostReadNewsView, \
    RecommendedNewsView, \
    LatestNewsView, \
    GlobalNewsView, \
    InquiryNewsView, \
    ArticleNewsView, \
    AdvertisementsView, NewsDetailView

urlpatterns = [
    path("<str:slug>", NewsDetailView.as_view(), name="news_detail"),
    path("main/", MainNewsView.as_view(), name="main_news"),
    path("latest/", LatestNewsView.as_view(), name="latest_news"),
    path("global/", GlobalNewsView.as_view(), name="global_news"),
    path("inquiry/", InquiryNewsView.as_view(), name="inquiry_news"),
    path("article/", ArticleNewsView.as_view(), name="article_news"),
    path("advertisements/", AdvertisementsView.as_view(), name="ads_news"),
    path("most_read/", MostReadNewsView.as_view(), name="most_read_news"),
    path("recommended/", RecommendedNewsView.as_view(), name="recommended_news"),

    ]
