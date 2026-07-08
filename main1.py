#haar nahi man sakta
#1 Create a variable for your faviorite food, a variable for how many times a week you eat it, and then use the print() to display them.

# Creating the variables
fav_food = "Dal"        #first variable 
times_in_a_week = 3     #second variable 

# Printing them by combining text and variables 
print("My faviorite food is", fav_food)
print("I eat it", times_in_a_week, "times in a week.")

# How would write a program that asks user for their name, and then print a personalized greeting?

user_name = input("Write your name : ")
print("Welcome to the Python world", user_name)
user_food = input("What is your faviorite food : ")
print("Oh wow! I love eating", user_food, "too,", user_name)

#Write a small program that asks the user for the current year, convert it to an integer,
#  sutracts their birth year, and prints out their approximate age.
current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))
# Calculate the approximate age
age = current_year - birth_year
print("Your approximate age is:", age)

user_age = int(input("Enter your age: "))
if user_age < 18:
    print("You are a teenager.")
elif user_age >= 18 and user_age <60:
    print("You are a working professional.")
else:
    print("You are a senior citizen.")
    