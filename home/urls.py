from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^shop/$', views.ShopView.as_view(), name='shop'),
    url(r'^shop/charge$', views.charge, name='charge'),
    url(r'^sponsors/$', views.SponsorsView.as_view(), name='sponsors'),
)
