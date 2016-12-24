from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<dataset_name>[-\w]+)$', views.IndexView.as_view(), name='index'),
	#url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^$', views.HomeView.as_view(), name='home'),
	url(r'^(?P<dataset_name>[-\w]+)/(?P<chart_type>[-\w]+)$', views.IndexView.as_view(), name='index'),
]