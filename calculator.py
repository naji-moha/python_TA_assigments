num1 = int(input("Enter  num1: "))
num2 = int(input("Enter num2: "))
operation= input ("What operation do you wanna do: ")

if operation == "addition":
	sum = num1+num2
	print("The addition of num1 and num2 is : " + str(sum))

elif operation == "subtraction": 
	sub= num1 - num2
	print("The subtraction of num1 and num2 is : " + str(sub))

elif operation =="division": 
	div= num1 / num2
	print("The division of num1 and num2 is : " + str(div))

elif operation == "multiplication":
	multip= num1 * num2
	print("The multiplication of num1 and num2 is : " + str(multip))

else:
	print ("Error")

