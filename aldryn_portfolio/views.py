# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Project,
	Artwork,
)


class ProjectCreateView(CreateView):

    model = Project


class ProjectDeleteView(DeleteView):

    model = Project


class ProjectDetailView(DetailView):

    model = Project


class ProjectUpdateView(UpdateView):

    model = Project


class ProjectListView(ListView):

    model = Project


class ArtworkCreateView(CreateView):

    model = Artwork


class ArtworkDeleteView(DeleteView):

    model = Artwork


class ArtworkDetailView(DetailView):

    model = Artwork


class ArtworkUpdateView(UpdateView):

    model = Artwork


class ArtworkListView(ListView):

    model = Artwork

