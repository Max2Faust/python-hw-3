import sys

def double_zero(array):
	if len(array) == 0:
		print ("Empty array")
		sys.exit()
	count = 0
	list = array.copy()
	for i in range(len(array)):
		try:
			if int(array[i]) == 0:
				list.insert(i+count, 0)
				count +=1
		except ValueError as err:
			print ('Invalid type of value :(')
			sys.exit()
	return list
#	print (list)

double_zero([1,0,2,3,0,4,5,0]) #-> [1,0,0,2,3,0,0,4,5,0,0]
double_zero([1,0,2,3,0,4,5,0]) #-> [1,0,0,2,3,0,0,4,5,0,0]
double_zero([1,2,3]) #-> [1,2,3]
