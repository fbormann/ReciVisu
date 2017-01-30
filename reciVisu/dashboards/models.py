from django.db import models
from autoslug.fields import AutoSlugField

class DataSet(models.Model):
	name = models.CharField("Nome", max_length= 200,unique=True)
	slug = AutoSlugField("Slug",populate_from='name',unique=True, default = "test")
	sector = models.CharField("setor", max_length= 200, blank=True)
	description = models.CharField("description", max_length= 300)
	url = models.URLField("url", max_length=400, default="/")

	def __str__(self):
		return self.name

class Variable(models.Model):
	name = models.CharField("nome", max_length= 200)
	dataset = models.ForeignKey(DataSet)
	variable_type = models.CharField("type", max_length= 200)

class DashBoard(models.Model):
	title = models.CharField("Titulo", max_length= 200,unique=True)
	data = models.ManyToManyField(DataSet, related_name = "datasets")

class Data(models.Model):
	"""
	Represents the instance of data inside the dataset, basically, files that hold the Data of a Dataset, 
	they possess urls and charts are built upon them
	"""
	name = models.CharField("Nome", max_length= 200,unique=True)
	slug = AutoSlugField("Slug",populate_from='name',unique=True)
	url = models.FileField("caminho", upload_to = "data/")

	dataset = models.ForeignKey(DataSet, related_name='dataset')
	