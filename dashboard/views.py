from django.shortcuts import render
from .models import *
def dashboard(request, subreddit):
	try:
		sub = Subreddit.objects.get(name=subreddit)
	except Subreddit.DoesNotExist:
		return render(request, "404.html")


