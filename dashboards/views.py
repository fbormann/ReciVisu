from django.shortcuts import render
from . import chartFactory
from django.views import generic

from django.http import JsonResponse

from .models import DataSet, Variable, Data
import pandas as pd
from django.views.generic import DetailView

from django.contrib.staticfiles.templatetags.staticfiles import static
"""
It returns the main deashboard menu
"""
class IndexView(generic.TemplateView):
    template_name = "dashboards/index.html"

    def get_context_data(self, **kwargs):
    	context = super(IndexView, self).get_context_data(**kwargs)
    	context['title'] = 'Know more about ' + kwargs['dataset_name']

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


class DatasetDetailView(DetailView):
    
    model = DataSet
    
    def get_context_data(self, **kwargs):

        context = super(DatasetDetailView, self).get_context_data(**kwargs)
        dataset = kwargs['object']
        variables = Variable.objects.filter(dataset = dataset)
        dataset_data = Data.objects.filter(dataset=dataset)
        context['variables'] = variables
        if len(variables) == 0 and len(dataset_data) > 0:
            data = pd.read_csv(dataset_data[0].url, sep=";", encoding="latin-1")
            print("vim aqui")
            for item in data.columns:

                v = Variable(name=item, dataset = dataset)
                v.save()

        """
        I'll log visitors after
        """
        return context



class HomeView(generic.TemplateView):
    template_name = "dashboards/home.html"

    def get_context_data(self, **kwargs):
    	context = super(HomeView, self).get_context_data(**kwargs)
    	context['title'] = 'Bem-vindo ao Recife Visu'
    	context['datasets'] = DataSet.objects.all()
    	
    	return context