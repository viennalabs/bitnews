from django.contrib import admin
from .models import Link, Vote # relative import is considered good practice. Import our own Models.

class LinkAdmin(admin.ModelAdmin): # use built-in ModelAdmin with it's default
	pass
admin.site.register(Link, LinkAdmin)

class VoteAdmin(admin.ModelAdmin):
	pass
admin.site.register(Vote, VoteAdmin)