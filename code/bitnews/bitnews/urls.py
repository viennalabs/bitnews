from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# Views
from links.views import LinkListView, UserProfileDetailView, UserProfileEditView

# Decorator to make profile edit page accessable only when logged in
from django.contrib.auth.decorators import login_required as auth

# URLs
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bitnews.views.home', name='home'),
    # url(r'^bitnews/', include('bitnews.foo.urls')),
    url(r'^$', LinkListView.as_view(), name='home'), # ^ and $ refer to beginning and end of string

    url(r'^login/$', 'django.contrib.auth.views.login',
    	{'template_name': 'login.html'},
    	name="login"
    ),

    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
    	name="logout"
    ),

    url(r'^accounts/', include('registration.backends.simple.urls'), # don't define the ending ($) to allow for 'sub-urls'
    ),

    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(),
    	name="profile"
    ),

    # wrap this url in auth to make sure only logged in user can edit his profile
    url(r'^edit_profile/$', auth(UserProfileEditView.as_view()),
    	name="edit_profile"
    ),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),


)
