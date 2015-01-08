from django import forms

from .models import UserProfile, Link

# users can edit profile info through this form
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ("user") # we don't want to give the user the option who to sign in as!

# users submit links through this form
class LinkForm(forms.ModelForm):
	class Meta:
		model = Link
		exclude = ("submitter", "rank_score") # we don't want those to appear on the form
		