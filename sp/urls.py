from django.conf.urls.defaults import *
from sp.views import home_page
from django.contrib import admin
admin.autodiscover()
from sp.microcons.views import micro_cons, micro_done
from sp.article.views import latest_articles, view_article
from sp.props.views import edit_article

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', home_page), 
	(r'^admin/', include(admin.site.urls)),
	(r'^micro_constitution/$', micro_cons),
	(r'^done/$', micro_done),
	(r'^latest/$', latest_articles),
	(r'^latest/(\d+)/$', view_article),
	(r'^edit/(\d+)/$', edit_article),

    # Examples:
    # url(r'^$', 'sp.views.home', name='home'),
    # url(r'^sp/', include('sp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
