from django.urls import path, include
from .views import *

urlpatterns = [
	path('ticker-mentions', upload_ticker_mentions, name="api_upload_ticker_mentions"),
	path('dashboard', include('dashboard.urls'))
]
