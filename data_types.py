#Data types - Strings, Numbers (Int, Float), Boolean(True | False)

#Strings
name = "Alice"
greeting = f"Hi, {name}!"

#Numbers
num = 10
num_decimal = 20.67

#Boolean
is_student = True
age = 20
driver_licence = True
can_drive = age >= 18 and driver_licence
print(can_drive)
day = "Wednesday"
is_weekend = day == "Saturday" or day == "Sunday"
print("Is weekend:", is_weekend)

# Check different types
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>

# Check variables
age = 25
name = "Alice"
print(type(age))         # <class 'int'>
print(type(name))        # <class 'str'>

temparature = 20
if temparature > 30:
    print("Its too hot!")
elif temparature > 25:
    print("Its hot!")
else:
    print("Its nice weather!")