
from django import forms
from .models import DataSet, Data
class DataSetForm(forms.ModelForm):
    class Meta:
        model = DataSet
        fields = ('name', 'description' , 'sector',)
    
class DataForm(forms.ModelForm):
	class Meta:
		model = Data
		fields = ('name', 'url', 'dataset')