def argmin(lst):
	return min(range(len(lst)), key=lst.__getitem__)