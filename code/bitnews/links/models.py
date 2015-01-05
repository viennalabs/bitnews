from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
	"""docstring for Link"""
	title = models.CharField("Headline", max_length=100)		
	submitter = models.ForeignKey(User) # ForeignKey refers to the User modul we've imported from django.contrib.auth.models
	submitted = models.DateTimeField(auto_now_add=True) 
	rank_score = models.FloatField(default=0.0)
	url = models.URLField("URL", max_length=250, blank=True) # if the URL is blank we assume a selfpost and ...	
	description = models.TextField(blank=True) # ... store the Text for the selfpost

	def __unicode__(self):
		return self.title

class Vote(models.Model):
	"""docstring for Vote"""
	voter = models.ForeignKey(User)			
	link = models.ForeignKey(Link)

	def __unicode__(self):
		return "%s upvoted %s" % (self.voter.username, self.link.title)