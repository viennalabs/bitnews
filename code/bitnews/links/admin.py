from django.contrib import admin
from .models import Link, Vote, UserProfile # relative import is considered good practice. Import our own Models.

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

class LinkAdmin(admin.ModelAdmin): # use built-in ModelAdmin with it's default
	pass
admin.site.register(Link, LinkAdmin) # let's use our new class so we can access it from the Admin interface

class VoteAdmin(admin.ModelAdmin):
	pass
admin.site.register(Vote, VoteAdmin)

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False

class UserProfileAdmin(UserAdmin):
	inlines = (UserProfileInline, )

admin.site.unregister(get_user_model()) # unregister existing user admin
admin.site.register(get_user_model(), UserProfileAdmin) # register our new user admin
