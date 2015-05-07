from rest_framework import serializers
from image_scrap.models import ImageScrap, History
from django.contrib.auth.models import User


class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('pk', 'images', 'date', 'nums')


class ImageScrapSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageScrap
        fields = ('pk', 'url', 'description', 'time')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'password')