from rest_framework.views import APIView
from django.http import HttpResponse, Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from image_scrap.models import ImageScrap, History
from image_scrap.serializers import HistorySerializers, ImageScrapSerializers, UserSerializers
from abc import ABCMeta
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.views.generic import FormView
from forms import ImageForm


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class RestListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication,)
    __metaclass__ = ABCMeta
    serializer = None
    query_set = None

    def get(self, request):
        data = self.query_set
        serializer = self.serializer(data, many=True)
        return JSONResponse(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = self.serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


class RestDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication,)
    __metaclass__ = ABCMeta
    serializer = None
    model = None

    def get_object(self, pk):
        try:
            data = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404
        return data

    def get(self, request, pk):
        data = self.get_object(pk)
        serializer = self.serializer(data)
        return JSONResponse(serializer.data)

    def put(self, request, pk):
        data = self.get_object(pk)
        data_request = JSONParser().parse(request)
        serializer = self.serializer(data, data=data_request)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        data = self.get_object(pk)
        data.delete()
        return HttpResponse(status=204)


class ImageListView(RestListView):
    query_set = ImageScrap.objects.all()
    serializer = ImageScrapSerializers

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = self.serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            if History.objects.filter(date=timezone.now().date()).exists():
                history = History.objects.get(date=timezone.now().date())
            else:
                history = History.objects.create()
            history.images.add(ImageScrap.objects.last())
            history.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


class ImageDetailView(RestDetailView):
    model = ImageScrap
    serializer = ImageScrapSerializers


class HistoryDetailView(RestDetailView):
    model = History
    serializer = HistorySerializers


class HistoryListView(RestListView):
    query_set = History.objects.all()
    serializer = HistorySerializers

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = self.serializer(data=data)
        history_exists = History.objects.filter(date=timezone.now().date()).exists()
        if history_exists:
            return JSONResponse({'error': 'Today history is exists'})
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


class HistoryListViewToday(HistoryListView):
    query_set = History.objects.filter(date=timezone.now().date())
    serializer = HistorySerializers


class ImageListViewToday(ImageListView):
    query_set = ImageScrap.objects.filter(history__date=timezone.now().date())
    serializer = ImageScrapSerializers


class UserListView(APIView):
    query_set = User.objects.all()
    serializer = UserSerializers
    permission_classes = (AllowAny,)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = self.serializer(data=data)
        user = authenticate(**serializer.initial_data)
        if user is None and serializer.is_valid():
            user = User.objects.create_user(**serializer.data)
        elif user is None and not serializer.is_valid():
            return JSONResponse(serializer.errors, status=400)
        token = Token.objects.get_or_create(user=user)
        return JSONResponse({'auth_token': token[0].key}, status=201)


class SomeImage(FormView):
    template_name = 'image_scrap/index.html'
    form_class = ImageForm