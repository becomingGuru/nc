from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # Example:
    # (r'^nikecup/', include('nikecup.foo.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'register/$','reg.views.register',name='register'),
    url(r'registered/(?P<pk>\d+)/$','reg.views.registered',name='registered'),
    url(r'download/(?P<pk>\d+)/$','reg.views.download',name='download_pdf'),
    url(r'download-offline/$','reg.views.download_slno_only',name='download_offline'),
    url(r'page2/(?P<pk>\d+)/$','reg.views.page2',name='pdf_page2'),
    url(r'registered-pdf/(?P<team_hash>\d+)/$','reg.views.download_pdf_hash',name='download_pdf_hash'),
    url(r'teams/$','reg.views.teams_redirect',name='teams_redirect'),
    url(r'downloads/$','reg.views.downloads_redirect',name='downloadss_redirect'),
    url(r'payment/(?P<team_hash>\d+)/$','reg.views.payment',name='payment'),
    url(r'payment-done/$','reg.views.payment_done',name='payment_done'),
    url(r'paymentpk/(?P<pk>\d+)/$','reg.views.paymentpk',name='paymentpk'),
    url(r'/payment-thanks/$',direct_to_template,
        {'template':'payment_thanks.html'},
        name='payment_thanks'),
    url(r'/payment-fail/$',direct_to_template,
        {'template':'payment_fail.html'},
        name='payment_fail'),
)

from django.conf import settings
import os

if settings.SERVE_MEDIA:
    urlpatterns += patterns('', 
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.PROJECT_ROOT,'media/')})
    )
