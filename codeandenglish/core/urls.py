from django.conf.urls import url

from codeandenglish.core.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]
