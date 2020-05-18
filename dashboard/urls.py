from django.urls import path, include
from .views import *
urlpatterns = [
	path('<str:subreddit>', dashboard, name="dashboard"),
]
