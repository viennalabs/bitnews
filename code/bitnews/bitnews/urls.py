from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# Views
# from links.views import LinkListView, UserProfileDetailView, UserProfileEditView, LinkCreateView, LinkDetailView, LinkUpdateView, LinkDeleteView
# instead of importing every object individually from views I import the whole file,
# and adress them as views.<object> rather than just <object>
from links import views

# Decorator to make profile edit page accessable only when logged in
from django.contrib.auth.decorators import login_required

# URLs
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bitnews.views.home', name='home'),
    # url(r'^bitnews/', include('bitnews.foo.urls')),
    url(r'^$', 
        views.LinkListView.as_view(), 
        name='home'
    ),

    url(r'^login/$', 
        'django.contrib.auth.views.login',
    	{'template_name': 'login.html'},
    	name="login"
    ),

    url(r'^logout/$', 
        'django.contrib.auth.views.logout_then_login',
    	name="logout"
    ),

    url(r'^accounts/', 
        include('registration.backends.simple.urls'), # don't define the ending ($) to allow for 'sub-urls'
        # not sure about the name since this is an 'open-ended' url
    ),

    url(r'^users/(?P<slug>\w+)/$', 
        views.UserProfileDetailView.as_view(),
    	name="profile"
    ),

    url(r'^edit_profile/$', 
        login_required(views.UserProfileEditView.as_view()),
    	name="edit_profile"
    ),

    url(r'^link/create/$', login_required(views.LinkCreateView.as_view()),
        name="link_create"
    ),

    url(r'^link/(?P<pk>\d+)$', # pk: primary key. SQLite rows are numbered on creation date
        views.LinkDetailView.as_view(),
        name="link_detail"
    ),

    url(r'^link/update/(?P<pk>\d+)/$',
        login_required(views.LinkUpdateView.as_view()),
        name="link_update"
    ),

     url(r'^link/delete/(?P<pk>\d+)/$',
        login_required(views.LinkDeleteView.as_view()),
        name="link_delete"
    ),

     url(r'^comments/',
        include('django.contrib.comments.urls')
    ),

    url(r'^admin/doc/', 
        include('django.contrib.admindocs.urls')
    ),
    url(r'^admin/', 
        include(admin.site.urls)
    ),  
)
