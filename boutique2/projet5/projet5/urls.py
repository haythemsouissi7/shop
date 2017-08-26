from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from authentication import views as bootcamp_auth_views
from settings import views as core_views



from reaction import views as react_views

from notification import views as notification_views
from collection import views as col_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^authontication/', include('authentication.urls')),
    url(r'^boutique/', include('produit.urls')),
    url(r'^album/', include('album.urls')),
    url(r'^profile/', include('settings.urls')),
    url(r'^discover/', include('discover.urls')),
    url(r'^collection/', include('collection.urls')),
    url(r'^promotion/', include('promotion.urls')),

    url(r'^api/creation/', include("creation.api.urls", namespace='creation-api')),
    url(r'^api/produit/', include("produit.api.urls", namespace='produit-api')),
    url(r'^api/notification/', include("notification.api.urls", namespace='notification-api')),
    url(r'^api/reaction/', include("reaction.api.urls", namespace='reaction-api')),
    url(r'^api/message/', include("messenger.api.urls", namespace='message-api')),



    url(r'^col/$', col_views.collection, name='collection'),
    url(r'^create/$', col_views.create_collection, name='create'),
    
    
    url(r'^login', auth_views.login, {'template_name': 'core/cover.html'},
        name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', bootcamp_auth_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/picture/$', core_views.picture, name='picture'),
    url(r'^settings/upload_picture/$', core_views.upload_picture,
        name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', core_views.save_uploaded_picture,
        name='save_uploaded_picture'),
    url(r'^settings/password/$', core_views.password, name='password'),


    url(r'^messages/', include('messenger.urls')),
    
   

    url(r'^settings/(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),


    
    


    url(r'^notifications/$', notification_views.notifications,
        name='notifications'),
    url(r'^notifications/last/$', notification_views.last_notifications,
        name='last_notifications'),
    url(r'^notifications/check/$', notification_views.check_notifications,
        name='check_notifications'),
   
  
    url(r'^react/(?P<pk>\d+)/$', react_views.react, name='react'),
    url(r'^Nreaction/(?P<produit_id>\d+)/$', react_views.Nreaction, name='Nreaction'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)