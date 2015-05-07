from django.conf.urls import url
from image_scrap import views


urlpatterns = [
    url(r'^image/$', views.ImageListViewToday.as_view()),
    url(r'^image/all/$', views.ImageListView.as_view()),
    url(r'^image/(?P<pk>[0-9]+)/$', views.ImageDetailView.as_view()),
    url(r'^history/$', views.HistoryListViewToday.as_view()),
    url(r'^history/all/$', views.HistoryListView.as_view()),
    url(r'^history/(?P<pk>[0-9]+)/$', views.HistoryDetailView.as_view()),
    url(r'^user/$', views.UserListView.as_view())]