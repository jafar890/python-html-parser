from django.views import generic
from html_parse.forms import ParseForm
from html_parse.parser import parser_function


class ParseView(generic.FormView):
    template_name = 'html_parse.html'
    form_class = ParseForm


class ShowParseView(generic.TemplateView):
    template_name = 'show_parse.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        image, price = parser_function(self.request.GET.get('url'))
        ctx['image'] = image
        ctx['price'] = price
        return ctx

