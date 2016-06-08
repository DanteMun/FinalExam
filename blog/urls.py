from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^category/(?P<pk>\d+)/$', 'blog.views.category_detail', name='category_detail'),
    url(r'^shop/(?P<pk>\d+)/$', 'blog.views.shop_detail', name='shop_detail'),

]