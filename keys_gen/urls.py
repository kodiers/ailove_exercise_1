from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^get-key/$', views.get_key, name='get_key'),
    url(r'^repaid-key/$', views.repaid_key, name='repaid_key'),
    url(r'^key-info/(?P<pk>\d+)/$', views.key_info, name='key_info'),
    url(r'^keys-count/$', views.keys_count, name='keys_count'),
]