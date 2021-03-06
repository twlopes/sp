from django.conf.urls.defaults import *
from sp.views import *
from django.contrib import admin
admin.autodiscover()
from sp.microcons.views import micro_cons, micro_done
from django.contrib.auth.views import login, logout
from sp.article.views import view_article
from sp.props.views import create_prop, view_article_props, view_latest_props, view_single_prop, prop_accept
from sp.accounts.views import register, register_done, profile
from sp.voting.views import up_vote, down_vote

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url('^', include('follow.urls')),
	(r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
	(r'^accounts/profile/$', profile),
	(r'^register/$', register),
	(r'^register_done/$', home),
	(r'^home/$', home),
	(r'^insta_links/$', insta_links),
	(r'^$', insta_links),
	(r'^admin/', include(admin.site.urls)),
	(r'^micro_constitution/$', micro_cons),
	(r'^done/$', micro_done),
	(r'^latest/$', latest_articles),
	(r'^articles/(\d+)/$', view_article),
	(r'^edit/(\d+)/$', create_prop),
	(r'^props/(\d+)/$', view_article_props),
	(r'^latestprops/$', view_latest_props),
	(r'^prop/(\d+)/$', view_single_prop),
	(r'^propaccept/(\d+)/$', prop_accept),
	(r'^prop/(\d+)/up/$', up_vote),
	(r'^prop/(\d+)/down/$', down_vote),
	(r'^hot/$', hot),

    # Examples:
    # url(r'^$', 'sp.views.home', name='home'),
    # url(r'^sp/', include('sp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)