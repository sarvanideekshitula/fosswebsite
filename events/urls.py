from django.conf.urls import url



urlpatterns = [
    url(r'^Event/(?P<pk>[0-9]+)', Event, name='Event'),
]