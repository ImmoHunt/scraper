from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Item, Comment, ChatUser

 

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = {"username", "email", "password1", "password2"}

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


"""class ArticleForm(ModelForm):
	class Meta:
	    model = item
	    fields = [ 'item_title', 'item_content', 'item_published', 'item_series',
			'item_slug', 'item_photo', 'item_video']
"""
class CommentForm(forms.ModelForm):
	comment_title = forms.CharField(help_text="Please enter title of your comment.")
	comment_content = forms.CharField(help_text="Please write your comment.")
	comment_date = forms.DateField(help_text="Please date of your comment.")
	class Meta:
		model = Comment
		fields = {"comment_title", "comment_content", "comment_date", "comment_item", "comment_author"}
	def clean_rec_data(self):
		title_data = self.cleaned_data['comment_title']
		content_data = self.cleaned_data['comment_content']
		date_data = self.cleaned_data['comment_date']
		
		if date_data > datetime.date.today():
			raise ValidationError(_('Invalid date - it cannot be in the future'))
		if title_data == '':
			raise ValidationError(_('Invalid value in title, please fill it up'))
		if content_data == '':
			raise ValidationError(_('Invalid content, please fill it up'))
		full_data = self.cleaned_data['comment_title', 'comment_content', 'comment_date']
		return full_data

class CreateChatUser(forms.ModelForm):
	ChatUser_nick = forms.CharField(help_text="Please enter your blog nick", label="Nick")
	ChatUser_fname = forms.CharField(help_text="Please enter your first name", label="First name")
	ChatUser_lname = forms.CharField(help_text="Please enter your last name", label="Last name")
	ChatUser_email = forms.CharField(help_text="Please enter your email", label="Email")
	ChatUser_dob = forms.DateField(help_text="Please enter your date of birth", label="Date of birth")
	ChatUser_password = forms.CharField(widget=forms.PasswordInput, help_text="Please enter your password", label="Password")
	class Meta:
		model = ChatUser
		fields = {"ChatUser_nick", "ChatUser_fname", "ChatUser_lname", "ChatUser_email", "ChatUser_dob", "ChatUser_password"}
	def clean_rec_data(self):
		full_data = self.cleaned_data['ChatUser_nick', 'ChatUser_fname', 'ChatUser_lname', 'ChatUser_email', 'ChatUser_dob', 'ChatUser_password']
		return full_data
