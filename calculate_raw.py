import sys



#if len(sys.argv) != 4 or len(sys.argv) !=2:
#    print('Arg len should be 4')
#    sys.exit()

# +, -, /, *

# ['L3/src/calculate.py', '2', '+', '2']
# [лівий операнд] [ариф опер] [правий опера]

# PEP-8
allowed_operations = ['+', '-', '/', '*', '%']
operation = ""
if len(sys.argv) == 4:
	left_operand = sys.argv[1]
	right_operand = sys.argv[3]
	operation = sys.argv[2]
elif len(sys.argv) == 2:
	for  i in allowed_operations:
		str = sys.argv[1].split(i)
		if len(str) == 2:
			operation = i
			left_operand = str[0]
			right_operand = str[1]
			break
else:
	print ("Usage: calculate.py [лівий операнд][ариф опер][правий опера]")
	sys.exit()


if operation not in allowed_operations:
    print('Operation is not allowed')
    sys.exit()
try:
    left_operand = int(left_operand)
    right_operand = int(right_operand)
except ValueError:
    print('Left and Right operands must be int')
    sys.exit()

if operation == '/' and right_operand == 0:
    print('Division by zero is not allowed')
    sys.exit()

## Option 1
def calc(left_operand, right_operand, operation):
	if operation == '*':
	     return(left_operand * right_operand)
	elif operation == '+':
	     return(left_operand + right_operand)
	elif operation == '-':
	     return(left_operand - right_operand)
	elif operation == '/':
	     return(left_operand / right_operand)
	elif operation == '%':
	     return(left_operand % right_operand)

print (calc(left_operand, right_operand, operation))

## Option 2
# match operation:
#     case '*':
#         print(left_operand * right_operand)
#     case '+':
#         print(left_operand + right_operand)


## Option 3
# print(eval(f'{left_operand}{operation}{right_operand}'))


# def perform_operation(left, right, operation)
#     return ()


    





