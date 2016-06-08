from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.shop_detail', name='shop_detail'),

]