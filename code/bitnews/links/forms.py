from django import forms
from .models import UserProfile

# custom form mainly bc we don't want to show user option
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ("user") # we don't want to give the user the option who to sign in as!