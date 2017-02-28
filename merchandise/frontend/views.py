from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Template View for the Index page."""

    template_name = "index.html"