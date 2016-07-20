#scheduling functions

# schedule_function has 3 params-
# 1) the function you want to schedul
# 2) how often
# 3) when you want it to happen time wise
# for example:
# schedule_function(weekly_trades, date_rules.week_end(), time_rules.market_close(minutes=30))


#this example takes a long position in SPY at the start of the week, and then closes out the position at 3:30 on the last day of the week:

def initialize(context):
	context.spy = sid(8554)

	schedule_function(open_positions, date_rules.week_start(), time_rules.market_open())
	schedule_function(close_positions, date_rules.week_end(), time_rules.market_close(minutes=30))

def open_positions(context, data):
	order_target_percent(context.spy, 0.10)

def close_positions(context, data):
	order_target_percent(context.spy, 0)

#managing portfolio
# current portfolio is stored in context.portfolio.positions
# for example, if we wanted to close all of our open positions:
	for security in context.portfolio.positions:
		order_target_percent(security,0)

# so, order_target_percent(security,0) sells all

# you can also plot series:

def initialize(context):
	context.aapl = sid(24)
	context.spy = sid(8554)
	
	schedule_function(rebalance, date_rules.every_day(), time_rules.market_open())
	schedule_function(record_vars, date_rules.every_day(), time_rules.market_close())

def rebalance(context, data):
	order_target_percent(context.aapl, 0.50)
	order_target_percent(context.spy, -0.50)

def record_vars(contet, data):
	long_count = 0
	short_count = 0

	for position in context.portfolio.positions.itervalues():
		if position.amount > 0:
			long_count += 1
		if position.amount < 0:
			short_count += 1

	#plot the counts here:

	record(num_long=long_count,num_short=short_count)