import requests
import datetime
import csv
import time
import json

# Global Variables
url = "http://localhost:8000/api/"
common_stock_names = {"slack": "WORK", "apple": "AAPL", "disney": "DIS", "facebook": "FB", "microsoft": "MSFT", "tesla": "TSLA", "netflix": "NFLX", "amazon": "AMZN", "google": "GOOGL"}
weird_tickers = ["IQ", "CEO", "DD",'EOD', "DOW", "EU","HAS", "MA", "BRO",  "EAT", "WORK", "TEAM",'ACRE', 'ACT', 'AGO',  'AIR', 'AL', 'ALE', 'ALEC', 'ALEX', 'ATH',  'ALL', 'ALLY', 'ALT', 'AM', 'AN', 'AND', 'ANTE', 'ANY', 'APEX', 'AQUA','ARC', 'ARCH', 'ARE', 'ARGO', 'ASH', 'AT', 'ATOM', 'AUTO', 'AVID', 'AX', 'AXE', 'BAM', 'BAND', 'BE', 'BEAM', 'BEAT', 'BEN', 'BEST', 'BIG', 'BILL', 'BIT', 'BLUE', 'BOND', 'BOOM', 'BOOT', 'BOX', 'BUD', 'BUG', 'BY', 'CAKE', 'CALM', 'CAMP', 'CAR', 'CAN', 'CARE', 'CASH', 'CAT', 'CENT', 'CHEF', 'CHI', 'CIG', 'CLUB', 'COG', 'COKE', 'COLD', 'CONE', 'COO', 'COOP', 'COP', 'CORE', 'COST', 'CRY', 'CUB', 'CUBA', 'CUBE', 'CUE', 'CYAN', 'DAN', 'DARE', 'DECK', 'DISH', 'DOG', 'DOOR', 'DORM', 'DUG', 'DUO', 'EARN', 'EAST', 'ECHO', 'ED', 'EDIT', 'EGO', 'EH', 'EL', 'ELF', 'ELSE', 'ERA', 'ERIC', 'ERIE', 'EROS', 'ES', 'EVA', 'EVER', 'EYE', 'FAD', 'FAM', 'FANG', 'FARM', 'FAST', 'FAT', 'FATE', 'FICO', 'FIVE', 'FIX', 'FLAT', 'FLEX', 'FLOW', 'FLY', 'FOE', 'FOLD', 'FOR', 'FORD', 'FORK', 'FORM', 'FORTY', 'FUN', 'FUND', 'GAIN', 'GEL', 'GENE', 'GIVE', 'GLAD', 'GO', 'GOLD', 'GOLD', 'GOLF', 'GOOD', 'GRAM', 'GRID', 'GRIN', 'GROW', 'GULF', 'GUT', 'GYRO', 'HA', 'HALL', 'HARP', 'HE', 'HEAR', 'HERD', 'HERO', 'HI', 'HOLD', 'HOME', 'HONE', 'HOOK', 'HOPE', 'HUD', 'HUGE', 'ICE', 'ICON', 'ING', 'INN', 'IO', 'IT', 'JACK', 'JAN', 'JAZZ', 'JOE', 'KEN', 'KEY', 'KIDS', 'KIM', 'KIN', 'KIRK', 'KO', 'LAD', 'LAKE', 'LAND', 'LARK', 'LAZY', 'LEAF', 'LEE', 'LEG', 'LEO', 'LIFE', 'LIN', 'LITE', 'LIVE', 'LOAN', 'LOB', 'LOCO', 'LONE', 'LOOP', 'LOVE', 'LOW', 'LUNA', 'LUNG', 'MA', 'MAC', 'MAIN', 'MAN', 'MARK', 'MAS', 'MATH', 'MEET', 'MEN', 'MET', 'MIN', 'MIND', 'MINT', 'MINT', 'MIST', 'MITT', 'MOD', 'MORN', 'MR', 'NAN', 'NE', 'NEAR', 'NEO', 'NEON', 'NET', 'NEW', 'NEWT', 'NEXT', 'NICE', 'NICK', 'NINE', 'NOAH', 'NOVA', 'NOW', 'OIL', 'OLD', 'ON', 'ONE', 'ONTO', 'OR', 'ORA', 'ORC', 'OTIS', 'OUT', 'PAC', 'PACK', 'PAM', 'PAR', 'PEAK', 'PECK', 'PEER', 'PEG', 'PEN', 'PER', 'PHI', 'PHO', 'PI', 'PICO', 'PIE', 'PINE', 'PING', 'PLAN', 'PLAY', 'PLOW', 'PLUS', 'POOL', 'POST', 'PRO', 'PUB', 'PUMP', 'QUAD', 'RA', 'RACE', 'RAIL', 'RAMP', 'RAND', 'RARE', 'RAVE', 'RE', 'REAL', 'REED', 'REG', 'REV', 'REX', 'RICK', 'RIG', 'RING', 'RIO', 'RIOT', 'ROAD', 'ROCK', 'ROLL', 'ROSE', 'RUBY', 'RUN', 'RUTH', 'SA', 'SAFE', 'SAGE', 'SAIL', 'SALT', 'SAM', 'SAN', 'SAVE', 'SAVE', 'SE', 'SEE', 'SEED', 'SELF', 'SHE', 'SHEN', 'SHIP', 'SHY', 'SHY', 'SILK', 'SITE', 'SIX', 'SKY', 'SNAP', 'SO', 'SOL', 'SOLO', 'SON', 'SONG', 'SPAR', 'STAY', 'SUM', 'SUN', 'SUP', 'SURF', 'SYNC', 'TA', 'TAP', 'TD', 'TEAM', 'TECH', 'TELL', 'TEN', 'TERP', 'TH', 'THO', 'TILE', 'TIP', 'TOPS', 'TOT', 'TOUR', 'TOWN', 'TREE', 'TRIP', 'TRUE', 'TURN', 'TUSK', 'TWIN', 'TWO', 'UN', 'UNIT', 'VALE', 'VEGA', 'VERB', 'VERY', 'VET', 'WASH', 'WEI', 'WELL', 'WIRE', 'WOOD', 'WORK', 'WOW', 'WU', 'YIN', 'ZEAL', 'ZEUS', 'ZION', 'ZYME']
ticker_freq = {}

with open('all_tickers.csv', mode='r') as infile:
	all_tickers = [row["Symbol"] for row in csv.DictReader(infile)]

def checkifticker(word):
	if word in all_tickers:
		return True
	return False

def add_to_dict(word):
	if word in ticker_freq:
		ticker_freq[word] += 1
	else:
		ticker_freq[word] = 1

def process_comment(comment):
		words = comment.split()
		for word in words:
			if len(word) == 1:
				continue
			# Check if the word is possibly a properly formatted ticker first
			if word[0] == "$":
				if len(word[1:]) < 6:
					word = word[1:].upper()
					if checkifticker(word):
						add_to_dict(word)
				continue
			# Could be a word that is commonly used to refer to a popular stock
			if word.lower() in common_stock_names:
				word = word.lower()
				ticker = common_stock_names[word]
				add_to_dict(ticker)
				continue
			# Word that is less than 6 characters and made of all letters is very possibly a ticker,
			# and it shouldn't be a word that is just a normal word capitalized
			if len(word) < 6 and word.isalpha() and word.upper() not in weird_tickers:
				word = word.upper()
				if checkifticker(word):
					add_to_dict(word)

def process_all_comments(data):
	for comment in data:
		process_comment(comment["body"])

def combine_dicts(dict1, dict2):
	ret = {}
	unique_keys = [x for x in dict1.keys() if x not in dict2.keys()] + [x for x in dict2.keys() if x not in dict1.keys()]
	for key in unique_keys:
		if key in dict1:
			ret[key] = dict1[key]
		if key in dict2:
			ret[key] = dict2[key]
	set1 = set(dict1)
	set2 = set(dict2)
	for key in set1.intersection(set2):
		ret[key] = dict1[key] + dict2[key]
	return ret

def request_comment_data(begin, end):
	try:
		resp = requests.get(
			'https://api.pushshift.io/reddit/search/comment/?subreddit=wallstreetbets&metadata=true&size=1000&after={0}&before={1}'.format(
				begin, end)).json()
		return resp
	except json.decoder.JSONDecodeError:
		time.sleep(10)
		resp = request_comment_data(begin, end)
		return resp

# Main
week = ['M', 'T',  'W', 'Th', 'F', 'S', 'Su']
begin = 1577682000
total_time = 0
spy = 0
number_of_spys = 0
for i in range(1):
	total_posts = 0
	day_freq = {}
	for j in range(24):
		process_time = time.time()
		for k in range(12):
			end = begin + 300
			resp = request_comment_data(begin, end)
			posts = resp['metadata']['total_results']
			total_posts += posts
			process_all_comments(resp['data'])
			time.sleep(1)
			while posts > 1000:
				new_begin = resp['data'][-1]['created_utc'] + 1
				resp = request_comment_data(new_begin, end)
				posts = resp['metadata']['total_results']
				total_posts += posts
				process_all_comments(resp['data'])
				time.sleep(1)
			if 'SPY' in ticker_freq:
				print(ticker_freq['SPY'], begin)
				spy += ticker_freq['SPY']
			data = {
				"tickers": json.dumps(ticker_freq),
				"time": begin
			}
			requests.post(url + "ticker-mentions", data=data)

			begin += 300 #increment 5 minutes
			day_freq = combine_dicts(day_freq, ticker_freq)
			ticker_freq.clear()
	print(week[i], day_freq)
	print(spy, number_of_spys)

	# by_freq = sorted(day_freq, key=day_freq.get, reverse=True)
	begin += 3600*14
