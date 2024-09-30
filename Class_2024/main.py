x=10 #Global variable can be access anywhere

def outer_function():
 print(f"Value of x in outer function {x}")
 x=20 # Enclosing variable
 print(f"Value of x in outer function after modification")
def inner_function():
        print(f"Value of x in inner function before modification is{x}")
        x=30 #Local Variable
        print(f"Value in inner function after modification {x} ") #Output:30
inner_function()
print(x) #Output:20§


print(x) #Output:10

outer_function()
print(x)
