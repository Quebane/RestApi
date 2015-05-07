from rest_framework import serializers
from image_scrap.models import ImageScrap, History


class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('pk', 'images', 'date', 'nums')


class ImageScrapSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageScrap
        fields = ('pk', 'url', 'description', 'time')