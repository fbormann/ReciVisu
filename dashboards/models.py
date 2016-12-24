from django.db import models


class DataSet(models.Model):
	name = models.CharField("Nome", max_length= 200,unique=True)
	url = models.FileField("caminho", upload_to = "data/")
	sector = models.CharField("setor", max_length= 200, blank=True)

class DashBoard(models.Model):
	title = models.CharField("Titulo", max_length= 200,unique=True)
	data = models.ManyToManyField(DataSet, related_name = "datasets")


