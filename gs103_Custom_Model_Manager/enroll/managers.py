from django.db import models

class CustomManager(models.Manager): #ikada Manager anedi by default ga django esthundi.Manager is parent and CustomManager anedi chaild
	def get_queryset(self):
		return super().get_queryset().order_by('name')
		#return super().get_queryset().order_by('roll')	