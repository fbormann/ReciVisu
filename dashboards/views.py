from django.shortcuts import render
from . import chartFactory
from django.views import generic

from django.contrib.staticfiles.templatetags.staticfiles import static
"""
It returns the main deashboard menu
"""
class IndexView(generic.TemplateView):
    template_name = "dashboards/index.html"

    def get_context_data(self, **kwargs):
    	context = super(IndexView, self).get_context_data(**kwargs)
    	context['title'] = 'Bem-vindo ao ReciVisu'

    	script, div = chartFactory.bar_chart('dashboards/static/datasets/156_cco_2016.csv', 'SITUACAO') #TODO: solve this path problem
    	context['dataset_name'] = '156_cco_2016.csv'
    	context['div'] = div
    	context['script'] = script
    	return context