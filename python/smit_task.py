## Finding prime numbers ##

a = int(input("Enter Your number"))

if a % a == 0:
    print(f"{a} this number is Prime")
else:
    print(f"{a} this number is not a prime number")

## Finding prime numbers ##

## Creating a program using if, else, and elif statements ##

email_input = input("Enter your email")
email = "abc@gmail.com"
name = "Wahaj"
contact = "+92123123"
password_input = input("Enter your password")
password = "123"

if email_input == email or email_input == contact and password_input == password:
    print(f"{name} your email/contact and password are matched")
elif email_input == email or email_input == contact and password_input != password:
    print(f"{name} your email/contact are matched but password are wrong")
elif email_input != email or email_input != contact:
    print(f"{name} your email and contact are not found")
else:
    print("Something went wrong. Try again.")

## Creating a program using if, else, and elif statements ##

## Developing a grading system program ##

marks = int(input("Enter Your marks"))

if marks >= 90:
    print("Your grade is A+")
elif marks >= 80:
    print("Your grade is A")
elif marks >= 70:
    print("Your grade is B")
elif marks >= 60:
    print("Your grade is C")
elif marks >= 50:
    print("Your grade is D")
else:
    print("Fail")

## Developing a grading system program ##