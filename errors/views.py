from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class PageNotFound(TemplateView):
    template_name = 'errors/404.html'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault("status", 404)
        return super().render_to_response(context, **response_kwargs)


class UnderConstruction(TemplateView):
    template_name = "errors/under-construction.html"
