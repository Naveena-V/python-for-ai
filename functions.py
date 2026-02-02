def check_weather():
    temparature = 16
    if temparature > 20:
        print("Its Hot!!")
    else:
        print("Nice Weather!!")
check_weather()

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")
greet("Alice", "Jill")
greet(last_name="Jhon", first_name="Jwane")

#default values for functions
def check_params(first_name="Dave", last_name="Jhon"):
    print(f"Hello, {first_name} {last_name}!")
check_params()
check_params("Chris")

#Returning value from functions
def calcualte_sum(num1, num2):
    return num1 + num2
sum = calcualte_sum(10, 20)
print(sum)

def simple_function():
    numbers = [1,2,3,4,5,6,7]
    first_num = numbers[0]
    last_num = numbers[-1]
    return first_num, last_num
f,l = simple_function()
print("F:", f)
print("L", l)