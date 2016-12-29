from django.shortcuts import render
from . import chartFactory
from django.views import generic

from django.http import JsonResponse

from django.shortcuts import redirect
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
    		script, div = chartFactory.make_chart(dataset_path =  'dashboards/static/dashboards/data/'+kwargs['dataset_name']+'.csv', 
    		 chart_type = kwargs['chart_type']) #TODO: solve this path problem
    		context['dataset_name'] = kwargs['dataset_name']
    		context['div'] = div
    		context['script'] = script
    	elif kwargs.get('dataset_name'):
    		script, div = chartFactory.make_chart('dashboards/static/dashboards/data/'+kwargs['dataset_name']+'.csv') #TODO: solve this path problem
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


class PlotVariableView(generic.TemplateView):
    template_name = 'dashboards/variable.html'

    def get_context_data(self, **kwargs):
        context = super(PlotVariableView, self).get_context_data(**kwargs)
        context['title'] = 'Know more about ' + kwargs['variable_name']
        if kwargs.get('dataset_name') and kwargs.get('variable_name'):
            #try:
            if kwargs.get('chart_type'):
                script, div = chartFactory.make_chart(dataset_path = 'dashboards/static/dashboards/data/'+kwargs['dataset_name']+'.csv',
                var_name = kwargs['variable_name'], chart_type= kwargs['chart_type'] ) #TODO: solve this path problem
            else:
                dataset_name = kwargs.get('dataset_name')
                variable_name = kwargs.get('variable_name')
                script, div = chartFactory.make_chart(dataset_path = 'dashboards/static/dashboards/data/'+dataset_name+'.csv', var_name = variable_name) #TODO: solve this path problem
            
            context['dataset_name'] = kwargs['dataset_name']
            context['chart_types'] = chartFactory.return_variables_types(dataset_path = 'dashboards/static/dashboards/data/'+kwargs['dataset_name']+'.csv',
                 var_name = kwargs['variable_name'])
            context['div'] = div
            context['script'] = script
            context['variable_name'] = kwargs['variable_name']
            #except:
                 #redirect('dashboards:detail', slug=kwargs['dataset_name'])
        else:
            redirect('dashboards:detail', slug=kwargs['dataset_name'])

        return context

class HomeView(generic.TemplateView):
    template_name = "dashboards/home.html"

    def get_context_data(self, **kwargs):
    	context = super(HomeView, self).get_context_data(**kwargs)
    	context['title'] = 'Bem-vindo ao Recife Visu'
    	context['datasets'] = DataSet.objects.all()
    	
    	return context