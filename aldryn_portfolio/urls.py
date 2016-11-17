# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^Project/~create/$",
        view=views.ProjectCreateView.as_view(),
        name='Project_create',
    ),
    url(
        regex="^Project/(?P<pk>\d+)/~delete/$",
        view=views.ProjectDeleteView.as_view(),
        name='Project_delete',
    ),
    url(
        regex="^Project/(?P<pk>\d+)/$",
        view=views.ProjectDetailView.as_view(),
        name='Project_detail',
    ),
    url(
        regex="^Project/(?P<pk>\d+)/~update/$",
        view=views.ProjectUpdateView.as_view(),
        name='Project_update',
    ),
    url(
        regex="^Project/$",
        view=views.ProjectListView.as_view(),
        name='Project_list',
    ),
	url(
        regex="^Artwork/~create/$",
        view=views.ArtworkCreateView.as_view(),
        name='Artwork_create',
    ),
    url(
        regex="^Artwork/(?P<pk>\d+)/~delete/$",
        view=views.ArtworkDeleteView.as_view(),
        name='Artwork_delete',
    ),
    url(
        regex="^Artwork/(?P<pk>\d+)/$",
        view=views.ArtworkDetailView.as_view(),
        name='Artwork_detail',
    ),
    url(
        regex="^Artwork/(?P<pk>\d+)/~update/$",
        view=views.ArtworkUpdateView.as_view(),
        name='Artwork_update',
    ),
    url(
        regex="^Artwork/$",
        view=views.ArtworkListView.as_view(),
        name='Artwork_list',
    ),
	]
