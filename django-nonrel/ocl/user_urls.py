from django.conf.urls.defaults import patterns, url
from conceptcollections.views import CollectionListView, CollectionRetrieveUpdateDestroyView, CollectionVersionListView, CollectionVersionRetrieveUpdateView, CollectionVersionRetrieveUpdateDestroyView, CollectionVersionChildListView
from orgs.views import OrganizationListView
from sources.views import SourceListView, SourceRetrieveUpdateDestroyView, SourceVersionRetrieveUpdateView, SourceVersionChildListView, SourceVersionListView, SourceVersionRetrieveUpdateDestroyView
from users.views import UserDetailView

__author__ = 'misternando'

extra_kwargs = {'user_is_self': True}

urlpatterns = patterns('',
    url(r'^$', UserDetailView.as_view(), extra_kwargs, name='user-self-detail'),
    url(r'^orgs/$', OrganizationListView.as_view(), extra_kwargs, name='user-organization-list'),
    url(r'^collections/$', CollectionListView.as_view(), extra_kwargs, name='user-source-list'),
    url(r'^collections/(?P<collection>[a-zA-Z0-9\-]+)/$', CollectionRetrieveUpdateDestroyView.as_view(), extra_kwargs, name='user-collection-detail'),
    url(r'^collections/(?P<collection>[a-zA-Z0-9\-]+)/versions/$', CollectionVersionListView.as_view(), extra_kwargs, name='user-collectionversion-list'),
    url(r'^collections/(?P<collection>[a-zA-Z0-9\-]+)/latest/$', CollectionVersionRetrieveUpdateView.as_view(), {'user_is_self': True, 'is_latest': True}, name='user-collectionversion-latest'),
    url(r'^collections/(?P<collection>[a-zA-Z0-9\-]+)/(?P<version>[a-zA-Z0-9\-]+)/$', CollectionVersionRetrieveUpdateDestroyView.as_view(), extra_kwargs, name='user-collectionversion-detail'),
    url(r'^collections/(?P<collection>[a-zA-Z0-9\-]+)/(?P<version>[a-zA-Z0-9\-]+)/children/$', CollectionVersionChildListView.as_view(), extra_kwargs, name='user-collectionversion-child-list'),
    url(r'^sources/$', SourceListView.as_view(), extra_kwargs, name='user-source-list'),
    url(r'^sources/(?P<source>[a-zA-Z0-9\-]+)/$', SourceRetrieveUpdateDestroyView.as_view(), extra_kwargs, name='user-source-detail'),
    url(r'^sources/(?P<source>[a-zA-Z0-9\-]+)/versions/$', SourceVersionListView.as_view(), extra_kwargs, name='user-sourceversion-list'),
    url(r'^sources/(?P<source>[a-zA-Z0-9\-]+)/latest/$', SourceVersionRetrieveUpdateView.as_view(), {'user_is_self': True, 'is_latest': True}, name='user-sourceversion-latest'),
    url(r'^sources/(?P<source>[a-zA-Z0-9\-]+)/(?P<version>[a-zA-Z0-9\-]+)/$', SourceVersionRetrieveUpdateDestroyView.as_view(), extra_kwargs, name='user-sourceversion-detail'),
    url(r'^sources/(?P<source>[a-zA-Z0-9\-]+)/(?P<version>[a-zA-Z0-9\-]+)/children/$', SourceVersionChildListView.as_view(), extra_kwargs, name='user-sourceversion-child-list'),
)