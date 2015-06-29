from django.conf.urls import patterns, url
from django.conf import settings
from home import views
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^shop/charge$', views.charge, name='charge'),
    url(r'^shop/success$', views.SuccessView.as_view(), name='success'),
    url(r'^shop/declined$', views.DeclineView.as_view(), name='decline'),
    url(r'^shop/$', views.ShopView.as_view(), name='shop'),
    url(r'^sponsors/$', views.SponsorsView.as_view(), name='sponsors'),
    url(r'^events/$', views.EventsView.as_view(), name='events'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html', 'redirect_field_name': 'home.html'}, name='login'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^connect/$', views.ConnectUploadImage.as_view(), name='connect'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
