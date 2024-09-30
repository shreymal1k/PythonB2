# Taking Inputs from the user
num1=int(input("Enter A Number : "))
num2=int(input("Enter Second Number : "))

if num1%2  == 0 and num2%2 == 0:
    print("Num1 and Num2 are Even.")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Num1 and Num2 are Odd.")
else:
    print("One Is Odd and other is Even.")