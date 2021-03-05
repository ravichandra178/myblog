from myapp.models import Comment
from django.forms import ModelForm

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']