from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<slug>[-\w]+)$', views.DatasetDetailView.as_view(), name='detail'),

	#url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^$', views.HomeView.as_view(), name='home'),
	#url(r'^(?P<dataset_name>[-\w]+)/(?P<chart_type>[-\w]+)$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<dataset_name>[-\w]+)/(?P<variable_name>[-\w]+)$', views.PlotVariableView.as_view(), name='plot_variable'),
	url(r'^(?P<dataset_name>[-\w]+)/(?P<variable_name>[-\w]+)/(?P<chart_type>[-\w]+)$', views.PlotVariableView.as_view(), name='plot_variable'),

]