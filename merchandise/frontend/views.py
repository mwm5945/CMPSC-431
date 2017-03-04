from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Template View for the Index page."""

    template_name = "index.html"
    params = {
        'page_title': "Welcome!",
        'page_header': "THON Merchandise"
    }

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context