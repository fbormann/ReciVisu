from django.shortcuts import render
from . import chartFactory
from django.views import generic

from django.http import JsonResponse

from .models import DataSet

from django.contrib.staticfiles.templatetags.staticfiles import static
"""
It returns the main deashboard menu
"""
class IndexView(generic.TemplateView):
    template_name = "dashboards/index.html"

    def get_context_data(self, **kwargs):
    	context = super(IndexView, self).get_context_data(**kwargs)
    	context['title'] = 'Bem-vindo ao ReciVisu'

    	if kwargs.get('dataset_name') and kwargs.get('chart_type'):
    		script, div = chartFactory.make_chart(dataset_path = 'dashboards/static/datasets/'+kwargs['dataset_name']+'.csv', 
    		 chart_type = kwargs['chart_type']) #TODO: solve this path problem
    		context['dataset_name'] = kwargs['dataset_name']
    		context['div'] = div
    		context['script'] = script
    	elif kwargs.get('dataset_name'):
    		script, div = chartFactory.make_chart('dashboards/static/datasets/'+kwargs['dataset_name']+'.csv') #TODO: solve this path problem
    		context['dataset_name'] = kwargs['dataset_name']
    		context['div'] = div
    		context['script'] = script

    	return context



class HomeView(generic.TemplateView):
    template_name = "dashboards/home.html"

    def get_context_data(self, **kwargs):
    	context = super(HomeView, self).get_context_data(**kwargs)

    	context['datasets'] = DataSet.objects.all()
    	print(context['datasets'][0].name)
    	return context