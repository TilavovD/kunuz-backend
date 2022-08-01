from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.
from helpers.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=128)


class Region(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    sub_content = models.TextField()
    content = RichTextUploadingField(null=True)
    image = models.ImageField(upload_to="post_image/")

    tags = models.ManyToManyField(Tag, related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="posts")
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, related_name="posts", null=True, blank=True)

    views_count = models.PositiveIntegerField(default=0)

    is_selected = models.BooleanField(default=False)
    is_global = models.BooleanField(default=False)
    is_interview = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=False)
    is_inquiry = models.BooleanField(default=False)

    def __str__(self):
        return self.title
