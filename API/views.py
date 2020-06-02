from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
import json
import datetime
from pytz import timezone

@api_view(["POST"])
def upload_ticker_mentions(request):
	tickers = request.POST.get('tickers')
	if tickers:
		tickers_dict = json.loads(tickers)
		f = 0
		with open('text.txt', 'w') as txtfile:
			for name in tickers_dict:
				if name == "SPY":
					txtfile.write(str(tickers_dict[name]))
					f += tickers_dict[name]
				epoch = request.POST.get('time')
				try:
					t = datetime.datetime.fromtimestamp(int(epoch), tz=timezone("US/Eastern"))
					ticker_mentions.objects.create(name=name, mentions=tickers_dict[name], time=t)
				except Exception as e:
					print(e)
		if f != 0:
			print(f, request.POST.get('time'))
		return Response(status.HTTP_201_CREATED)

	return Response(status.HTTP_400_BAD_REQUEST)



