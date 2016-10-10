def data_type(arg):
	if isinstance(arg, bool):
		return arg
	elif arg is None:
		return 'no value'
	elif isinstance(arg, (str, unicode)):
		return len(arg)
	elif isinstance(arg, int):
		if arg == 100:
			return 'equal to 100'
		elif arg < 100:
			return 'less than 100'
		elif arg > 100:
			return 'more than 100'
	elif isinstance(arg, list):
		try:
			return arg[2]
		except IndexError:
			return None