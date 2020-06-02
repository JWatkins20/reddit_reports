from API.models import ticker_mentions

def find_and_sum_mentions(name, start_date, end_date, increment):

	tickers = ticker_mentions.objects.filter(name=name,
											 time__gte=start_date,
											 time__lt=end_date).order_by('time')
	begin = start_date
	total_mentions_per_hour = []
	while begin < end_date:
		hour_ahead = begin + increment
		tickers_mentions_in_hour = list(tickers.filter(time__gte=begin, time__lt=hour_ahead).order_by('time'))
		total_mentions = 0
		for ticker_mention in tickers_mentions_in_hour:
			total_mentions += ticker_mention.mentions
		total_mentions_per_hour.append(total_mentions)
		begin = hour_ahead
	return total_mentions_per_hour