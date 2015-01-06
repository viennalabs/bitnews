from django.views.generic import ListView # use ListView bc we have a list of objects

from .models import Link, Vote

class LinkListView(ListView):
	model = Link # model refers to the relative import .models

	# let's overwrite queryset to include with_votes, which calls our new model manager VoteCounter
	queryset = Link.with_votes.all()
	# paginate_by = 3
