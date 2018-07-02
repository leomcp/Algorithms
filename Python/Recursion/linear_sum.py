def linear_sum(s, n):
	if n == 0: 
		return 0
	else:
		return linear_sum(S, n-1) + s[n-1]