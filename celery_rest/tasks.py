from celery_rest import app
from image_scrap.models import History
from django.utils import timezone


@app.task(track_started=True)
def count():
    if History.objects.filter(date=timezone.now().date()).exists():
        history = History.objects.get(date=timezone.now().date())
        nums = history.nums
        history.nums = history.images.count()
        if history.nums != nums:
            history.save()
            print 'New nums is ' + str(history.nums)