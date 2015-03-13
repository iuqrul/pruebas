from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required

#admin.autodiscover()
from clientes.views import DownloadPDF

from .views import (
    LoginView, LogoutView,
    IndexView,
)

urlpatterns = patterns(
    '',

    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('clientes.urls')),
    url(r'^descargar/factura/(?P<pk>.*)$', login_required(DownloadPDF.as_view()), name='pdf'),
    url(r'^$', login_required(IndexView.as_view()), name='home'),
)

if settings.DEBUG:
    urlpatterns = patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
