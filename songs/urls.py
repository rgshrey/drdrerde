from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Songs page
    url(r'^songs/$', views.songs, name='songs'),
    # Page for an individual song
    url(r'^song/(?P<song_id>\d+)/$', views.song, name="song"),
]
