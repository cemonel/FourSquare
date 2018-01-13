from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search_page, name='search_page'),
    url(r'^venue_detail/(?P<venue_id>[a-zA-Z0-9]+)/$', views.venue_detail, name='venue_detail'),
]
