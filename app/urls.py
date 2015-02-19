from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'app.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'app.views.home', name='home'),
					   url(r'^home/', 'app.views.home', name='home'),
                       url(r'^campaign/(?P<id>\d+)/', 'app.views.campaign_detail', name="campaign_detail"),
					   url(r'^thank_you/', 'app.views.thank_you', name="thank_you"),
                       url(r'^merchandise', 'app.views.merchandise', name='merchandise'),
                       url(r'^tickets', 'app.views.tickets', name='tickets'),
                       url(r'^schedule', 'app.views.schedule', name='schedule'),
                       # url(r'^admin/', include(admin.site.urls)),
)
