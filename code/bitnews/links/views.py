from django.views.generic import ListView, DetailView # use ListView bc we have a list of objects
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy

from django.contrib.auth import get_user_model

from .models import Link, Vote, UserProfile
from .forms import UserProfileForm, LinkForm

# the front page view
class LinkListView(ListView):
	model = Link # model refers to the relative import .models
	# let's overwrite queryset to include with_votes, 
	# which calls our new model manager VoteCounter
	queryset = Link.with_votes.all()
	paginate_by = 10

# a users profile page
class UserProfileDetailView(DetailView):
	model = get_user_model()
	slug_field = "username"
	template_name = "user_detail.html"

	def get_object(self, queryset=None):
		user = super(UserProfileDetailView, self).get_object(queryset)
		UserProfile.objects.get_or_create(user=user)
		return user

# users enter info about themselfes here
class UserProfileEditView(UpdateView):
	model = UserProfile
	form_class = UserProfileForm
	template_name = "edit_profile.html"

	def get_object(self, queryset=None):
		return UserProfile.objects.get_or_create(user=self.request.user)[0]

	def get_success_url(self):
		return reverse("profile", 
			kwargs={'slug': self.request.user})

# submit a link in this view
class LinkCreateView(CreateView):
	model = Link
	form_class = LinkForm

	# we need to save all the fields that we excluded in forms.py
	# 
	def form_valid(self, form):
		f = form.save(commit=False) # don't commit to the database just yet ...
		f.rank_score = 0.0
		f.submitter = self.request.user
		f.save() # ... do it now
						
		return super(LinkCreateView, self).form_valid(form)

# submission details including comment section
class LinkDetailView(DetailView):
	model = Link			

# an admin can change a submission
class LinkUpdateView(UpdateView):
	model = Link
	form_class = LinkForm

# an admin can delete a submission:
class LinkDeleteView(DeleteView):
	model = Link
	success_url = reverse_lazy("home")





