from rest_framework import status
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework.decorators import api_view
import json
from .helpers import *

@api_view(["GET"])
def get_mentions_over_period(request):
	name = request.POST.get('name')
	interval = request.POST.get('interval')
	start_epoch = int(request.POST.get('start_date'))
	end_epoch = int(request.POST.get('end_date'))
	start = datetime.fromtimestamp(start_epoch)
	end = datetime.fromtimestamp(end_epoch)

	increment = timedelta(hours=1)
	if interval == "5mins":
		increment = timedelta(minutes=5)
	elif interval == "15mins":
		increment = timedelta(minutes=15)
	elif interval == "day":
		increment = timedelta(days=1)
	elif interval == "week":
		increment = timedelta(weeks=1)

	all_mentions = find_and_sum_mentions(name, start, end, increment)
	data = {"mentions": json.dumps(all_mentions)}
	return Response(data, status=status.HTTP_200_OK)









