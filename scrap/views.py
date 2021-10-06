from django.shortcuts import render, redirect
from .models import imggal, Test, Item, ItemCategory, ItemSeries, Comment
from django.http import HttpResponse
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm, CommentForm, CreateChatUser
from .serializers import ItemSerializer
from rest_framework import generics

#def imagedisplay(request):
#    resultdisplay=imggal.objects.all()
#    return render(request, 'index.html', {'imggal':resultdisplay})
# Create your views here.

def single_slug(request, single_slug):
	comments = Comment.objects.all()
	categories = [c.category_slug for c in ItemCategory.objects.all()]
	if single_slug in categories:
		matching_series = ItemSeries.objects.filter(item_category__category_slug=single_slug)
		series_urls = {}

		for m in matching_series.all():
			part_one = Item.objects.filter(item_series__item_series=m.item_series).earliest("item_published")
			series_urls[m] = part_one.item_slug
		return render(request,
				"main/category.html",
				{"part_ones": series_urls})
	items = [i.item_slug for i in Item.objects.all()]
	if single_slug in items:
		this_item = Item.objects.get(item_slug=single_slug)
		comments = Comment.objects.filter(comment_item__item_title=this_item.item_title)
		this_item_title = this_item.item_title
		items_from_series = Item.objects.filter(item_series__item_series=this_item.item_series).order_by('item_published')
		this_item_idx = list(items_from_series).index(this_item)
		return render(request,
			"main/item.html",
			{"item": this_item,
			"comments": comments,
			"this_item_title": this_item_title,
			"sidebar": items_from_series,
			"this_item_idx": this_item_idx})
	return HttpResponse("{} does not correspond to anything we know of".format(single_slug))

def homepage(request):
	return render(request = request,
		template_name='main/categories.html',
		context = {"categories": ItemCategory.objects.all})
	#return HttpResponse("Funciona bem ainda! (vamos la cabrao)")
def community(request):
	return render(request = request,
	template_name='main/community.html',
	context={})
	#return redirect("/community")
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, "New account created: {}".format(username))
			login(request, user)
			messages.info(request, "You are now logged in as {}".format(user))
			return redirect("/")
			
		else:
			for msg in form.error_messages:
				messages.error(request, "{}: {}".format(msg, form.error_messages[msg]))
	
	form = NewUserForm
	return render(request,
			"main/register.html",
			context={"form":form})
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request = request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are now logged as {}".format(username))
				return redirect('/')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request = request,
			template_name = "main/login.html",
			context={"form":form})
def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("/")

def comment_request(request):
	#comment_instance = get_object_or_404(BookInstance, pk
	#CommentFilled = request.title	
	if request.method =="POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			Comment = form.save(commit=False)
			#here temporary for user
			#Comment.comment_author = 1
			#here item that we are in currently should be assigned
			#Comment.comment_item = 1
			Comment.save()
	else:
		#messages.info(request, "Couldn't add your comment")
		form = CommentForm()
	return render(request =  request,
			template_name = "main/comment.html",
			context={"form": form})

def chatuser_request(request):
	if request.method =="POST":
		form = CreateChatUser(request.POST)
		if form.is_valid():
			ChatUser = form.save(commit=False)

			ChatUser.save()
	else:
		#messages.info(request, "Couldn't create new blog user")
		form = CreateChatUser()
	return render(request = request,
		template_name = "main/chatuser.html",
		context={"form": form})

"""def add_post(request):
	if request.method == "POST":
		form = ArticleForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('')
			messages.success(request, "New account created: {}".format(username))
			login(request, user)
			messages.info(request, "You are now logged in as {}".format(user))
			return redirect("/")
			
		else:
			for msg in form.error_messages:
				messages.error(request, "{}: {}".format(msg, form.error_messages[msg]))
	
	form = NewUserForm
	return render(request,
			"main/register.html",
			context={"form":form})
"""
