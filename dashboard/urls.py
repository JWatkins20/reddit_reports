from django.urls import path
from .views import *
urlpatterns = [
	path('get-mentions-over-period', get_mentions_over_period, name="get-mentions-over-period"),
]
