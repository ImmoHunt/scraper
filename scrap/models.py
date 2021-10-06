from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms

class imggal(models.Model):
	imgtitle=models.CharField(max_length=100)
	imgdesc=models.CharField(max_length=500)
	image= models.ImageField(upload_to='scrap/media/images/')

class Test(models.Model):
	test_title = models.CharField(max_length=200)
	test_content = models.TextField()
	test_published = models.DateTimeField("date published", default=datetime.now())

	def __str__(self):
		return self.test_title

class ItemCategory(models.Model):
	item_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200, default=1)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.item_category

class ItemSeries(models.Model):
	item_series = models.CharField(max_length=200)
	item_category = models.ForeignKey(ItemCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Series"
	def __str__(self):
		return self.item_series

class Item(models.Model):
	item_id = models.IntegerField(primary_key=True, default=1)
	item_title = models.CharField(max_length=200)
	item_content = models.TextField()
	item_published = models.DateTimeField("date published",  default=datetime.now())
	#https://docs.djangoproject.com.en.2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
	item_series = models.ForeignKey(ItemSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	item_slug = models.CharField(max_length=200, default=1)
	item_photo = models.ImageField(upload_to='photos/',default='default.jpg', verbose_name="Minha foto", blank=True)
	item_video = models.FileField(upload_to='videos/',default='def_vid.mp4', verbose_name="Custom video", blank=True)	
	class Meta:
		verbose_name_plural = "Items"
	def __str__(self):
		return self.item_title

class ChatUser(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_nick = models.CharField(max_length=200)
	user_fname = models.CharField(max_length=200)
	user_lname = models.CharField(max_length=200)
	user_email = models.EmailField()
	user_dob = models.DateField()
	user_pass = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		verbose_name_plural = "ChatUsers"
	def __str__(self):
		return self.user_nick

class Comment(models.Model):
	comment_id = models.AutoField(primary_key=True)
	comment_item = models.ForeignKey(Item, default='Teste', verbose_name="Items", on_delete=models.SET_DEFAULT)
	#comment_item = models.IntegerField(default=1)
	comment_title = models.CharField(max_length=200)
	comment_content = models.TextField()
	comment_date = models.DateTimeField('comment date', default=datetime.now())
	comment_author = models.ForeignKey(ChatUser, default='immo', verbose_name="ChatUsers", on_delete=models.SET_DEFAULT)
	#comment_author = models.CharField(max_length=200)
	class Meta:
		verbose_name_plural = "Comments"
	def __str__(self):
		return self.comment_title
