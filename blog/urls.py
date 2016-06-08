from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),

    url(r'^category/(?P<pk>\d+)/$', 'blog.views.category_detail', name='category_detail'),
    url(r'^category/new/$', 'blog.views.category_new', name='category_new'),
    url(r'^category/(?P<pk>\d+)/edit/$', 'blog.views.category_edit', name='category_edit'),

    url(r'^shop/(?P<pk>\d+)/$', 'blog.views.shop_detail', name='shop_detail'),
    url(r'^shop/new/$', 'blog.views.shop_new', name='category_new'),
    url(r'^shop/(?P<pk>\d+)/edit/$', 'blog.views.shop_edit', name='shop_edit'),

    url(r'^shop/(?P<shop_pk>\d+)/review/new/$', 'blog.views.review_new', name='review_new'),
]