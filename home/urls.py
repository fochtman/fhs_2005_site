from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name="home"),
    '''
    url(r'^blog/$', views.BlogIndex.as_view(), name="index"),
    url(r'^blog/entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^feed/$', feed.LatestPost(), name="feed"),
    '''
)
