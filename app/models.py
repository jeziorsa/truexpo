from django.db import models
from django.forms import ModelForm

# Create your models here

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.project_name

class Image(models.Model):
    project = models.ForeignKey(Project)
    image_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects')
    def __unicode__(self):
        return self.image_title

class ImageForm(ModelForm):
    class Meta:
	model = Image
	exclude = ('project',)
