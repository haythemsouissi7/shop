from django.conf.urls import url

from messenger import views


urlpatterns = [

	url(r'^attache_image/$', views.attache_image, name='attache_image'),
	url(r'^search_modal/$', views.search_modal, name='search_modal'),
        url(r'^sendd/$', views.send2, name='send2'),
    url(r'^$', views.inbox, name='inbox'),
    url(r'^new/$', views.new, name='new_message'),
    url(r'^new_product/$', views.new2, name='new_product'),
    url(r'^send/$', views.send, name='send_message'),
    url(r'^delete/$', views.delete, name='delete_message'),
    url(r'^users/$', views.users, name='users_message'),
    url(r'^check/$', views.check, name='check_message'),
    url(r'^(?P<username>[^/]+)/$', views.messages, name='messages'),
   


]
