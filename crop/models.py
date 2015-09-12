from django.db import models

# Create your models here.
class videos(models.Model):
	title= models.CharField(max_length=50)
	timestamp= models.DateTimeField(auto_now_add=True)
	x=models.PositiveSmallIntegerField(default=0)
	y=models.PositiveSmallIntegerField(default=0)
	width=models.PositiveSmallIntegerField(default=0)
	height=models.PositiveSmallIntegerField(default=0)
	originalfile= models.CharField(max_length=500,blank=True,null=True)
	cropedfile= models.CharField(max_length=500,blank=True,null=True)

	def __unicode__(self):
		return "%s" % (self.title)

	class Meta:
		ordering = ['timestamp']