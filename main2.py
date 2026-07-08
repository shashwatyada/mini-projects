#Write a small script that loops exactly 5 times using a for loop. Inside that loop, use
#   an input() to ask the user for a number. Check if that number is Even or Odd, and print 
# the result.

for i in range(5):
    print(i)
    user_number = int(input("Enter a nuber: "))
    if user_number % 2 == 0:
        print("The number ", user_number, "is Even.")
    else:
        print("The number ", user_number, "is Odd.")

#1 Create a funtion called calculate_age that takes two parameters: current, birth.
#2 Inside the funtion, calculate age( current - birth).
#3 Print the final age out along with a nice message.
#4 Outside the fucntion, call it 2 or 3 times with different years to see it 
# calculate multiple ages instantly.

def calculate_age(c, b):
    age = c - b
    print("Your age is:", age)

calculate_age(2026, 1997)
calculate_age(2026, 1968)
c =int(input ("Enter the current year: "))
b =int(input ("Enter your bith year: "))
calculate_age(c, b)


