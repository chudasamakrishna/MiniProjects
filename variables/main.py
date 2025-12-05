# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains.

# Strings = A string is a series of character it can include number, we can treat it as a characters.
first_name = "Krishna"
food = "Pasta"
email = "soni.krishna9887@gmail.com"

print(f"Hii {first_name}.")
print(f"Do you like {food}?")
print(f"Let's Order {food}")
print(f"First you have to add your email {email} before ordering {food}")

# Integers
age = 24
quantity = 5
num_of_students = 30
print(f"You are {age} old.")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#Float
price = 20.5
cgpa = 8.65
distance = 50
print(f"The price is ${price}")
print(f"My cgpa is {cgpa}")
print(f"You ran {distance} km.")

#Boolean
is_student = False
if is_student:
    print("You are a student.")
else:
    print("You are not a student.")


for_sale = True
if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")