name = "Alice"
age = 20
is_student = True
score = 67.67
print("name:", name)
print("age:", age)
print("is_student:", is_student)
print("score:", score)
name = "Bob"
print("name is changed to:", name)
age = age + 6 + 1
print("Age is incremented by 7:", age)
def guess_age(age):
    if age < 10: 
        print("Age < 10")
    if age > 20:
        print("Age > 10 or < 20")

guess_age(8)
guess_age(21)