from django.conf.urls import url
from .views import WriteMemory, thanks, NewUserView, IndexView

urlpatterns = [
    url(r'^write/(?P<uuid>[^/]+)/$', WriteMemory.as_view(), name='write-memory'),
    url(r'^write/(?P<uuid>[^/]+)/(?P<type>[^/]+)/$', WriteMemory.as_view(), name='write-memory-type'),
    url(r'^thanks/$', thanks, name='thanks'),
    url(r'^new-user/$', NewUserView.as_view()),
    url(r'^$', IndexView.as_view(), name='index')
]