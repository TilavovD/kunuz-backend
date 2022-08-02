from rest_framework.serializers import ModelSerializer

from news.models import News, Tag, Category


class NewsListSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('title', "sub_content", "image", "created_at")

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)

class NewsDetailSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = News
        fields = ('title', "sub_content", "content", "image", "created_at", 'tags')
