name = input('Enter your name: ')
age  = input('Enter your age: ')
city = input('Enter your city: ')

# Print a sentence using name, age, city
print(f"Hello! I am {name}, {age} years old, from {city}.")

# Example output: Hello! I am Rahul, 22 years old, from Bangalore.





a = 42
b = 3.14
c = 'Python'
d = True
e = 0

# Store variables in a list to loop through them
variables = [a, b, c, d, e]

# Print the value and type of each variable
for var in variables:
    print(var, type(var))




age_str = '25'        # this is a string
# 1. Convert age_str to integer and print value + type
age_int = int(age_str)
print(age_int, type(age_int))

price = 199.99        # this is a float
# 2. Convert price to integer and print value + type
price_int = int(price)
print(price_int, type(price_int))

score = 1             # this is an integer
# 3. Convert score to boolean and print value + type
score_bool = bool(score)
print(score_bool, type(score_bool))

flag = True           # this is a boolean
# 4. Convert flag to integer and print value + type
flag_int = int(flag)
print(flag_int, type(flag_int))






user_input = input('Enter a number: ')

# Try to convert to int
try:
    value = int(user_input)
    print(f'You entered the number: {value}')
except ValueError:
    # If it fails, print error message
    print('That is not a valid number!')






# Take input from user (all will come as strings)
principal = input('Enter principal amount: ')
rate      = input('Enter interest rate (%): ')
time      = input('Enter time in years: ')

# Convert to correct data types
p = float(principal)
r = float(rate)
t = float(time)

# Calculate simple interest
interest = (p * r * t) / 100

# Calculate total amount = principal + interest
total_amount = p + interest

# Print both interest and total amount
print(f"Simple Interest: {interest}")
print(f"Total Amount:    {total_amount}")



def check_type(value):
    # Check boolean first because bool is a subclass of int
    if isinstance(value, bool):
        return "boolean"
    elif isinstance(value, int):
        return "integer"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, str):
        return "string"
    else:
        return "unknown type"

print(check_type(42))        # integer
print(check_type(3.14))      # float
print(check_type('hello'))   # string
print(check_type(True))      # boolean

