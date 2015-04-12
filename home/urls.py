from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^shop/$', views.ShopView.as_view(), name='shop'),
    url(r'^shop/charge$', views.charge, name='charge'),
    url(r'^sponsors/$', views.SponsorsView.as_view(), name='sponsors'),
    url(r'^events/$', views.EventsView.as_view(), name='events'),
    url(r'^connect/$', views.ConnectView.as_view(), name='connect'),
)
