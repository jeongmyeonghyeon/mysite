from django.conf.urls import url

from .views import BookmarkListView, BookmarkDetailView

urlpatterns = [
    url(r'^$', BookmarkListView.as_view(), name='index'),
    url(r'(?P<pk>\d+)/$', BookmarkDetailView.as_view(), name='detail')
]
