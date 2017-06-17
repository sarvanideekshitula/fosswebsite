from django.conf.urls import url

from events.views import Events

urlpatterns = [
    url(r'^Event/(?P<pk>[0-9]+)', Events, name='Events'),
]