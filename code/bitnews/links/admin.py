from django.contrib import admin
from .models import Link, Vote # relative import is considered good practice. Import our own Models.

class LinkAdmin(admin.ModelAdmin): # use built-in ModelAdmin with it's default
	pass
admin.site.register(Link, LinkAdmin) # let's use our new class so we can access it from the Admin interface

class VoteAdmin(admin.ModelAdmin):
	pass
admin.site.register(Vote, VoteAdmin)