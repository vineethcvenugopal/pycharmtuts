age = eval(input("Enter age: "))

if age < 5:
    print("You stay at home with mommy and daddy")

elif age == 5:
    print("You go to kindergarten")

elif (age > 5) and (age <= 17):
    grade = age - 5
    print("You go to grade {}".format(grade))

else:
    print("You go to College")


