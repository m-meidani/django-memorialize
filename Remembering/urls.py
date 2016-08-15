from django.conf.urls import url
from .views import WriteMemory, thanks

urlpatterns = [
    url(r'^write/(?P<uuid>[^/]+)/$', WriteMemory.as_view(), name='write-memory'),
    url(r'^write/(?P<uuid>[^/]+)/(?P<type>[^/]+)/$', WriteMemory.as_view(), name='write-memory'),
    url(r'^thanks/$', thanks, name='thanks'),
]