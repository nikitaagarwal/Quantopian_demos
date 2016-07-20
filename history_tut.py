def initialize(context):
	context.security_list = [sid(5061), sid(24)]

def before_trading_start(context, data):
	pass

def handle_data(context, data):
	data.history(context.security_list, 'close', 5, 'lm')
	#close price at the end of the last five minutes for each security in the list, cols are securities and rows are date times


	#get the 10-day trailing price history of SPY in the form of a series
	hist = data.history(sid(24), 'price', 10, '1d')

	#to get the last 10 complete days:
	data.history(sid(8554), 'volume', 11, '1d')[:-1].mean()

	#mean price over the last 10 days
	mean_price=hist.mean()