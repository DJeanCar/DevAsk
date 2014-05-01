from django.db import models
from django.template.defaultfilters import slugify
from apps.users.models import User

class TimeStampModel(models.Model):

	user = models.ForeignKey(User, db_index=True, null=True, blank=True)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	class Meta:
		abstract = True

class TagManager(models.Manager):

	def get_by_natural_key(self, nombre):
		return self.get(nombre=nombre)

class Tag(models.Model):

	nombre = models.CharField(max_length = 10)

	def __unicode__(self):
		return self.nombre


class Question(TimeStampModel):

	tag = models.ManyToManyField(Tag)
	title = models.CharField(max_length=200)
	slug = models.SlugField(editable = False, unique=True, null=True, blank=True)

	def __unicode__(self):
		return '%s %s' % (self.user , self.title)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Question, self).save(*args,**kwargs)


class Answer(TimeStampModel):

	question = models.ForeignKey(Question)

	def __unicode__(self):
		return self.user.username