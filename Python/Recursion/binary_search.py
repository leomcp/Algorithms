def binary_search(data, target, low, high):
	"""
	Return True if target if found in indicated portion 
	of a Python list. The search only considers the 
	portion from data[low] to data[high] inclusive.

	"""
	if low >  high:
		return False
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return True 
		elif target < data[mid]:
			# recur on th portion left of the middle 
			return binary_search(data, target, low, mid - 1)
		else:
			# recur on th portion right of the middle 
			return binary_search(data, target, mid + 1, high)

