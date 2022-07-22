import sys

def remove_duplicates(array):
	if len(array) == 0:
		print ("Empty array")
		sys.exit()
	list = []
	list.append(array[0])
	for i in range(1, len(array)):
		try:
			if int(array[i]) < int(array[i-1]):
				print ('Invalid list: not sorted')
				sys.exit()
			if int(array[i]) != int(array[i-1]):
				list.append(array[i])
		except ValueError as err:
			print ('Invalid value :(')
			sys.exit()
	print (list)

remove_duplicates([1,1,2]) # -> [1,2]
remove_duplicates([0,0,1,1,1,2,2,3,3,4]) # -> [0,1,2,3,4]
remove_duplicates([1,1,1,1,1,1,1,1]) # -> [1]
