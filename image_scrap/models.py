from django.db import models


class ImageScrap(models.Model):
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    time = models.TimeField(auto_now_add=True)

    def __unicode__(self):
        return self.url


class History(models.Model):
    images = models.ManyToManyField(ImageScrap)
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        result = 'List of image by ' + str(self.date) + ': '
        for image in self.images.all():
            result += image.url
        return result

    class Meta:
        verbose_name_plural = 'Histories'
        ordering = ['date']