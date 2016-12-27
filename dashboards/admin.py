from django.contrib import admin
from .forms import DataSetForm, DataForm
from .models import DataSet, Data
# Register your models here.
class DatasetAdmin(admin.ModelAdmin):
	list_display = ['name', 'sector', 'description', 'url']

	form = DataSetForm


class DataAdmin(admin.ModelAdmin):
	list_display = ['name', 'url']

	form = DataForm

admin.site.register(Data, DataAdmin)
admin.site.register(DataSet, DatasetAdmin)