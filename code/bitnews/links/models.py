from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

from django.db.models.signals import post_save


class VoteCounter(models.Manager):
	# we'll overwrite the get_query_set function
	def get_query_set(self):
		return	super(VoteCounter, self).get_query_set().annotate(
								votes=Count('vote')).order_by('-votes')

class Link(models.Model):
	title = models.CharField("Headline", max_length=100)
	submitter = models.ForeignKey(User) # ForeignKey refers to the User modul we've imported from django.contrib.auth.models
	submitted = models.DateTimeField(auto_now_add=True)
	rank_score = models.FloatField(default=0.0)
	url = models.URLField("URL", max_length=250, blank=True) # if the URL is blank we assume a selfpost and ...
	description = models.TextField(blank=True) # ... store the Text for the selfpost
	# let's do some vote counting magic
	with_votes = VoteCounter()
	objects = models.Manager() # default manager

	def __unicode__(self):
		return self.title

class Vote(models.Model):
	voter = models.ForeignKey(User)
	link = models.ForeignKey(Link)

	def __unicode__(self):
		return "%s upvoted %s" % (self.voter.username, self.link.title)

class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	# created =
	# karma =
	# average =
	bio = models.TextField(null=True)

	def __unicode__(self):
		return "%s's profile" % self.user

# Can we be sure that a user profile is created when a new user signs up?
# we can with ... signals
def create_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)

# Signal while saving user
post_save.connect(create_profile, sender=User)
