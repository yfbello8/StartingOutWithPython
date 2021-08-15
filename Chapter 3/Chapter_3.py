print("\t Chapter 3 - Decision Structures and Boolean Logic")
print("This program displays the Programming Challenges in Chapter 3")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 1 - Day of the Week")
print("Write a program that asks the user for a number in the range of 1 \
through 7. The program should display the corresponding day of the week, \
where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, \
6 = Saturday, and 7 = Sunday. The program should display an error message if \
the user enters a number that is outside the range of 1 through 7.")
print("")
day = int(input("Enter a number between 1 - 7: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day ==4:
    print("Thursday")
elif day == 5: 
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("ERROR: Selection must be an integer between 1 and 7!")

print("")

enter = input ("Press enter to continue")
print("")

print("Question 2 - Areas of Rectangles")
print("The area of a rectangle is the rectangle’s length times its width. \
Write a program that asks for the length and width of two rectangles. The \
program should tell the user which rectangle has the greater area, or if the \
areas are the same")
print("")

length_1 = float(input("Enter the length of the first rectangle: "))
width_1 = float(input("Enter the width of the first rectangle: "))
area_1 = length_1 * width_1

length_2 = float(input("Enter the length of the second rectangle: "))
width_2 = float(input("Enter the width of the second rectangle: "))
area_2 = length_2 * width_2

if area_1 > area_2:
    print("Rectangle 1 has a greater area")
elif area_2 > area_1:
    print("Rectangle 2 has a greater area")
elif area_1 == area_2:
    print("The rectangles have the same area")

print("")

enter = input ("Press enter to continue")
print("")

print("Question 3 - Age Classifier")
print("Write a program that asks the user to enter a person’s age. The program \
should display a message indicating whether the person is an infant, a child, \
a teenager, or an adult. Following are the guidelines:")
print("")
print("- If the person is 1 year old or less, he or she is an infant")
print("- If the person is older than 1 year, but younger than 13 years, he or \
she is a child")
print("- If the person is at least 13 years old, but less than 20 years old, \
he or she is a teenager")
print("If the person is at least 20 years old, he or she is an adult")
print("")
age = int(input("Enter your age: "))

if age <= 1:
    print("You are an infant")
elif age > 1 and age < 13:
    print("You are a child")
elif age > 13 and age < 20:
    print("You are a teenager")
elif age > 20:
    print("You are an adult")

print("")

enter = input ("Press enter to continue")
print("")

print("Question 4 - Roman Numerals")
print("Write a program that prompts the user to enter a number within the \
range of 1 through 10. The program should display the Roman numeral version \
of that number. If the number is outside the range of 1 through 10, the \
program should display an error message. The following table shows the Roman \
numerals for the numbers 1 through 10:")
print("")
print("Number ", "Roman Numeral", sep='     ')
print("1", "I", sep='           ')
print("2", "II", sep='           ')
print("3", "III", sep='           ')
print("4", "IV", sep='           ')
print("5", "V", sep='           ')
print("6", "VI", sep='           ')
print("7", "VII", sep='           ')
print("8", "VIII", sep='           ')
print("9", "IX", sep='           ')
print("10", "X", sep='          ')
print("")
num = int(input("Enter a number from 1 - 10: "))

if num == 1:
    print("I")
elif num == 2:
    print("II")
elif num == 3:
    print("III")
elif num == 4:
    print("IV")
elif num == 5:
    print("V")
elif num == 6:
    print("VI")
elif num == 7:
    print("VII")
elif num == 8:
    print("VIII")
elif num == 9:
    print("IX")
elif num == 10:
    print("X")
else:
    print("Error! Selection must be an integer between 1 and 10")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 5 - Mass and Weight")
print("Scientists measure an object’s mass in kilograms and its weight in \
newtons. If you know the amount of mass of an object in kilograms, you can \
calculate its weight in newtons with the following formula:")
print("")
print("weight = mass * 9.8")
print("")
print("Write a program that asks the user to enter an object’s mass, then \
calculates its weight. If the object weighs more than 500 newtons, display a \
message indicating that it is too heavy. If the object weighs less than 100 \
newtons, display a message indicating that it is too light")
print("")
mass = float(input("Enter an object's mass: "))
weight = mass * 9.8

if weight > 500:
    print("Object is too heavy!")
elif weight < 100:
    print("Object is too light!")

print("")

enter = input ("Press enter to continue")
print("")

# The book says in this question that the date is special because "the month 
# times the day equals the year," which is incorrect. it actually equals the 
# last two digits of the year 
print("Question 6 - Magic Dates")
print("The date June 10, 1960, is special because when it is written in the \
following format, the month times the day equals the year:")
print("6/10/60")
print("Design a program that asks the user to enter a month (in numeric form), \
a day, and a two-digit year. The program should then determine whether the \
month times the day equals the year. If so, it should display a message saying \
the date is magic. Otherwise, it should display a message saying the date is \
not magic")
print("")
month = int(input("Enter a month (1 for January, 2 for February, etc): "))
date = int(input("Enter a date: "))
year = int(input("Enter the last two digits of a year: "))
magic_num = month * date 

if magic_num == year:
    print("This number is a magic number!")
else:
    print("This number is not a magic number!")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 7 - Color Mixer")
print("The colors red, blue, and yellow are known as the primary colors \
because they cannot be made by mixing other colors. When you mix two \
primary colors, you get a secondary color, as shown here:")
print("")
print("- When you mix red and blue, you get purple")
print("- When you mix red and yellow, you get orange")
print("- When you mix blue and yellow, you get green")
print("")
print("Design a program that prompts the user to enter the names of two \
primary colors to mix. If the user enters anything other than “red,” “blue,” \
or “yellow,” the program should display an error message. Otherwise, the \
program should display the name of the secondary color that results")
print("")
color_1 = input("Enter a color you want to mix: ")
color_2 = input("Enter the second color you want to mix: ")

if color_1 == "red" and color_2 == "blue":
    print("The mixed color is purple")
elif color_1 == "blue" and color_2 == "red":
    print("The mixed color is purple")
elif color_1 == "red" and color_2 == "yellow":
    print("The mixed color is orange")
elif color_1 == "yellow" and color_2 == "red":
    print("The mixed color is orange")
elif color_1 == "yellow" and color_2 == "blue":
    print("The mixed color is green")
elif color_1 == "blue" and color_2 == "yellow":
    print("The mixed color is green")
else:
    print("ERROR! You have entered a color that is not red, yellow or blue. Please \
    check you spelling and capitalization")

print("")

enter = input ("Press enter to continue")
print("")

print("Question 8 - Hot Dog Cookout Calculator")
print("Assume hot dogs come in packages of 10, and hot dog buns come in \
packages of 8. Write a program that calculates the number of packages of hot \
dogs and the number of packages of hot dog buns needed for a cookout, with the \
minimum amount of leftovers. The program should ask the user for the number of \
people attending the cookout and the number of hot dogs each person will be \
given. The program should display the following details:")
print("")
print("- The minimum number of packages of hot dogs required")
print("- The minimum number of packages of hot dog buns required")
print("- The number of hot dogs that will be left over")
print("- The number of hot dog buns that will be left over")
print("")

# Calculate the number of hot dogs needed
people = int(input("Enter the number of people attending this party: "))
hotdogs_per_person = int(input("Enter the number of hot dogs each person will \
consume: "))
hotdogs_needed = hotdogs_per_person * people

# Calculate the number of packages of hot dogs needed, since there are 10 hot 
# dogs in a package
hotdog_packages_needed = hotdogs_needed // 10 

# If the remainder of the integer division above is not equal to 0, then add 1 
# more package. This is so we over serve and not under-serve
if hotdogs_needed % 10 != 0: 
    hotdog_packages_needed = hotdog_packages_needed + 1
# Calculate the remaining hot dogs
hotdogs_remainder = hotdogs_needed % 10 

# Calculate the number of packages of hot dog buns needed, since there are 8 
# hot dogs buns in a package
hotdog_buns_needed = hotdogs_needed // 8 
# If the remainder of the integer division above is not equal to 0, then add 1 
# more package. This is so we over serve and not under-serve
if hotdog_buns_needed % 8 != 0:
    hotdog_buns_needed += 1
# Calculate the remaining hot dog buns
hotdog_buns_remainder = hotdogs_needed % 8 

print("The minimum number of packages of hot dogs required:        ", \
    format(hotdog_packages_needed, ',d'))
print("The minimum number of packages of hot dog buns required:    ", \
    format(hotdog_buns_needed, ',d'))
print("The number of hot dogs that will be left over:              ", \
    format(hotdogs_remainder, ',d'))
print("The number of hot dog buns that will be left over:          ", \
    format(hotdog_buns_remainder, ',d'))
print("")

enter = input ("Press enter to continue")
print("")

print("Question 9 - Roulette Wheel Colors")
print("On a roulette wheel, the pockets are numbered from 0 to 36. The colors \
of the pockets are as follows:")
print("")
print("- Pocket 0 is green")
print("- For pockets 1 through 10, the odd-numbered pockets are red and the \
even-numbered pockets are black")
print("- For pockets 11 through 18, the odd-numbered pockets are black and the \
even-numbered pockets are red")
print("- For pockets 19 through 28, the odd-numbered pockets are red and the \
even-numbered pockets are black")
print("- For pockets 29 through 36, the odd-numbered pockets are black and the \
even-numbered pockets are red")
print("Write a program that asks the user to enter a pocket number and displays \
whether the pocket is green, red, or black. The program should display an error \
message if the user enters a number that is outside the range of 0 through 36")
print("")
pocket_num = int(input("Enter a pocket number: "))
remainder = pocket_num % 2

# This is a flag that sets if the number is even or odd
if remainder == 0:
    even = True
else:
    even = False

if pocket_num == 0:
    print("This pocket is green")
elif pocket_num > 0 and pocket_num < 11:
    if even: 
        print("This pocket is black")
    else:
        print("This pocket is red")
elif pocket_num > 10 and pocket_num < 19:
    if even:
        print("This pocket is red")
    else:
        print("This pocket is black")
elif pocket_num > 18 and pocket_num < 29:
    if even: 
        print("This pocket is black")
    else:
        print("This pocket is red")
elif pocket_num > 28 and pocket_num < 37:
    if even:
        print("This pocket is red")
    else:
        print("This pocket is black")
else:
    print("ERROR! Selection is out of range!")

print("")

enter = input ("Press enter to continue")
print("")

print("Question 10 - Money Counting Game")
print("Create a change-counting game that gets the user to enter the number of \
coins required to make exactly one dollar. The program should prompt the user \
to enter the number of pennies, nickels, dimes, and quarters. If the total \
value of the coins entered is equal to one dollar, the program should \
congratulate the user for winning the game. Otherwise, the program should \
display a message indicating whether the amount entered was more than or less \
than one dollar")
print("")
pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

if pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * .25 == 1.0:
    print("Congratulations! Those coins do make up a dollar!")
else:
    if pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * .25 > 1.0:
        print("These coins actually add to more than a dollar. Better luck next time")
    elif pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * .25 < 1.0:
        print("These coins actually add to less than a dollar. Better luck next time")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 11 - Book Club Points")
print("Serendipity Booksellers has a book club that awards points to its \
customers based on the number of books purchased each month. The points are \
awarded as follows:")
print("")
print("- If a customer purchases 0 books, he or she earns 0 points")
print("- If a customer purchases 2 books, he or she earns 5 points")
print("- If a customer purchases 4 books, he or she earns 15 points")
print("- If a customer purchases 6 books, he or she earns 30 points")
print("- If a customer purchases 8 or more books, he or she earns 60 points")
print("")
print("Write a program that asks the user to enter the number of books that he \
or she has purchased this month, then displays the number of points awarded")
print("")
books_purchased = int(input("Enter the number of books purchased this month: "))

if books_purchased == 0:
    print("Points earned: 0")
elif books_purchased > 2 and books_purchased < 5:
    print("Points earned: 5")
elif books_purchased > 4 and books_purchased < 7:
    print("Points earned: 15")
elif books_purchased > 6 and books_purchased < 9:
    print("Points earned: 30")
elif books_purchased > 8:
    print("Points earned: 60")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 12 - Software Sales")
print("A software company sells a package that retails for $99. Quantity \
discounts are given according to the following table:")
print("Quantity", "Discount", sep='     ')
print("10 - 19", "10%", sep='      ')
print("20 - 49", "20%", sep='      ')
print("50 - 99", "30%", sep='      ')
print("100 or more", "40$", sep='  ')
print("")
print("Write a program that asks the user to enter the number of packages \
purchased. The program should then display the amount of the discount \
(if any) and the total amount of the purchase after the discount")
print("")
quantity_purchased = int(input("Enter the number of packages purchased: "))

if quantity_purchased > 9 and quantity_purchased < 20:
    print("Discount: 10%")
elif quantity_purchased > 19 and quantity_purchased < 50:
    print("Discount: 20%")
elif quantity_purchased > 49 and quantity_purchased < 100:
    print("Discount: 30%")
elif quantity_purchased > 100:
    print("Discount: 40%")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 13 - Shipping Charges")
print("The Fast Freight Shipping Company charges the following rates:")
print("")
print("Weight of Package \t\t\t\t Rate per Pound")
print("2 pounds or less \t\t\t\t $1.50")
print("Over 2 pounds but not more than 6 pounds \t $3.00")
print("Over 6 pounds but not more than 10 pounds \t $4.00")
print("Over 10 pounds \t\t\t\t\t $4.75")
print("")
print("Write a program that asks the user to enter the weight of a package \
then displays the shipping charges")
weight = float(input("Enter the weight of a package: "))

if weight <= 2:
    rate = 1.5
elif weight > 2 and weight < 6:
    rate = 3.0
elif weight > 6 and weight < 10:
    rate = 4.0
elif weight > 10:
    rate = 4.75
else:
    print("ERROR! Selection cannot be processed. Try again")

shipping_charges = rate * weight

print("The shipping charges for this package is: $", format(shipping_charges, ',.2f'), sep='')
print("")

enter = input ("Press enter to continue")
print("")

print("Question 14 - Body Mass Index")
print("Write a program that calculates and displays a person’s body mass index \
(BMI). The BMI is often used to determine whether a person is overweight or \
underweight for his or her height. A person’s BMI is calculated with the \
following formula:")
print("BMI = weight * 703 / height^2")
print("where weight is measured in pounds and height is measured in inches. \
The program should ask the user to enter his or her weight and height, then \
display the user’s BMI. The program should also display a message indicating \
whether the person has optimal weight, is underweight, or is overweight. A \
person’s weight is considered to be optimal if his or her BMI is between 18.5 \
and 25. If the BMI is less than 18.5, the person is considered to be \
underweight. If the BMI value is greater than 25, the person is considered \
to be overweight")
print("")
weight = float(input("Enter the weight (in pounds): "))
height = float(input("Enter the height (in inches): "))

bmi = weight * 703 / height**2

print("BMI: ", format(bmi, '.2f'))

if bmi < 18.5:
    print("This person is considered underweight")
elif bmi >= 18.5 and bmi <= 25:
    print("This person is considered optimal")
elif bmi > 25:
    print("This person is considered overweight")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 15 - Time Calculator")
print("Write a program that asks the user to enter a number of seconds and \
works as follows:")
print("")
print("- There are 60 seconds in a minute. If the number of seconds entered by \
the user is greater than or equal to 60, the program should convert the number \
of seconds to minutes and seconds")
print("- There are 3,600 seconds in an hour. If the number of seconds entered \
by  the user is greater than or equal to 3,600, the program should convert the \
number of seconds to hours, minutes, and seconds")
print("- There are 86,400 seconds in a day. If the number of seconds entered by \
the user is greater than or equal to 86,400, the program should convert the \
number of seconds to days, hours, minutes, and seconds")
print("")
sec = int(input("Enter the number of seconds: "))

days = 0
hours = 0
min = 0
remainder = 0

if sec < 60:
    sec = sec
elif sec >= 60 and sec < 3600:
    min = sec // 60
    sec = sec % 60
elif sec >= 3600 and sec < 86400:
    hours = sec // 3600
    remainder = sec % 3600
    min = remainder // 60
    sec = remainder - (60 * min)
elif sec >= 86400:
    days = sec // 86400
    remainder = sec % 86400
    hours = remainder // 3600
    remainder = remainder % 3600
    min = remainder // 60
    sec = remainder - 60*min

    '''
This is the first way I tried - I was using complex if statements and nested ifs
until I was told that I could get rid of the if statements and make the whole 
thing much less complex. I have since simplified it and it works

if sec >= 86400:
    days = sec // 86400
    remainder = sec % 86400
    # This takes the remainder of the previous integer division (which would 
    # have been the decimal) and divides it by 3600 to find the hours
    hours = remainder // 3600
    remainder = remainder % 3600
    min = remainder // 60
    sec = remainder - (60 * min) 
elif sec >= 3600:
    hours = sec // 3600
    remainder = sec % 3600
    min = remainder // 60
    sec = remainder - (60 * min) 
elif sec >= 60:
    min = sec // 60
    sec = sec % 60
elif sec < 60:
    sec = sec

'''


print("Days:    ", days)
print("Hours:   ", hours)
print("Minutes: ", min)
print("Seconds: ", sec)

enter = input ("Press enter to continue")
print("")

print("Question 16 - February Days")
print("The month of February normally has 28 days. But if it is a leap year, \
February has 29 days. Write a program that asks the user to enter a year. The \
program should then display the number of days in February that year. Use the \
following criteria to identify leap years:")
print("")
print("1. Determine whether the year is divisible by 100. If it is, then it is \
a leap year if and only if it is also divisible by 400. For example, 2000 is \
a leap year, but 2100 is not")
print("2. If the year is not divisible by 100, then it is a leap year if and \
only if it is divisible by 4. For example, 2008 is a leap year, but 2009 is not")
print("")
print("Here is a sample run of the program:")
print("Enter a year: 2008 [ENTER]")
print("In 2008 February has 29 days")
print("")
year = int(input("Enter a year: "))

# This sets up flags to determine if the year is a leap year or not
if (year % 100) == 0:
    if (year % 400) == 0:
        is_leap_year = True
    else:
        is_leap_year = False
elif (year % 4) == 0:
    is_leap_year = True
else:
    is_leap_year = False

# This is the decision statement that executes based on the flags we have already set
if is_leap_year:
    print("The February in", year, "has 29 days")
else:
    print("The February in", year, "has 28 days")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 17 - Wi-Fi Diagnostic Tree")
print("Figure 3-19 shows a simplified flowchart for troubleshooting a bad Wi-Fi \
connection. Use the flowchart to create a program that leads a person through \
the steps of fixing a bad Wi-Fi connection. Here is an example of the \
program’s output:")
print("")
print("Reboot the computer and try to connect.")
print("Did that fix the problem? no [ENTER]")
print("Reboot the router and try to connect.")
print("Did that fix the problem? yes [ENTER]")
print("")
print("Notice the program ends as soon as a solution is found to the problem. \
Here is another example of the program’s output:")
print("")
print("Reboot the computer and try to connect.")
print("Did that fix the problem? no [ENTER]")
print("Reboot the router and try to connect.")
print("Did that fix the problem? no [ENTER]")
print("Make sure the cables between the router and modem are plugged in firmly.")
print("Did that fix the problem? no [ENTER]")
print("Move the router to a new location.")
print("Did that fix the problem? no [ENTER]")
print("Get a new router.")
print("")
print("Reboot the computer and try to connect")
choice = input("Did that fix the problem? ")
if choice == "no":
    print("Reboot the router and try to connect")
    choice = input("Did that fix the problem? ")

    if choice == "no":
        print("Make sure the cables between the router and modem are plugged \
        in firmly")
        choice = input("Did that fix the problem? ")

        if choice == "no":
            print("Move the router to a new location.")
            choice = input("Did that fix the problem? ")

            if choice == "no":
                print("Get a new router.")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 18 - Restaurant Selector")
print("You have a group of friends coming to visit for your high school \
reunion, and you want to take them out to eat at a local restaurant. You \
aren’t sure if any of them have dietary restrictions, but your restaurant \
choices are as follows:")
print("")
print("- Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No")
print("- Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes")
print("- Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes")
print("- Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No")
print("- The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes")
print("")
print("Write a program that asks whether any members of your party are \
vegetarian, vegan, or gluten- free, to which then displays only the \
restaurants to which you may take the group. Here is an example of the \
program’s output:")
print("")
print("Is anyone in your party a vegetarian? yes [ENTER]")
print("Is anyone in your party a vegan? no [ENTER]")
print("Is anyone in your party gluten-free? yes [ENTER]")
print("Here are your restaurant choices:")
print("\tMain Street Pizza Company")
print("\tCorner Cafe")
print("\tThe Chef's Kitchen")
print("")
print("Here is another example of the program’s output:")
print("Is anyone in your party a vegetarian? yes [ENTER]")
print("Is anyone in your party a vegan? yes [ENTER]")
print("Is anyone in your party gluten-free? yes [ENTER]")
print("Here are your restaurant choices:")
print("\tCorner Cafe")
print("\tThe Chef's Kitchen")
print("")
# Get the selection - I think the best way to do this is through the use of flags
veg_yn = input("Is anyone in your party a vegetarian? (Enter 'yes' or 'no'): ")
vegan_yn = input("Is anyone in your party a vegan? (Enter 'yes' or 'no'): ")
gf_yn = input("Is anyone in your party gluten-free? (Enter 'yes' or 'no'): ")

if veg_yn == "yes":
    is_veg = True
elif veg_yn == "no":
    is_veg = False
else:
    print("That selection is not an option! Please choose either 'yes' or 'no'")

if vegan_yn == "yes":
    is_vegan = True
elif vegan_yn == "no":
    is_vegan = False
else:
    print("That selection is not an option! Please choose either 'yes' or 'no'")

if gf_yn == "yes":
    is_gf = True
elif gf_yn == "no":
    is_gf = False
else:
    print("That selection is not an option! Please choose either 'yes' or 'no'")

print("Here are your restaurant choices:")

# Decision statements
if is_veg:
    #If you have vegetarians, exclude Joe's
    if is_gf:
        #If you have gluten-free members, exclude Mama's
        if is_vegan:
            #If you have vegan members, exclude Main Street
            print("\t Corner Café")
            print("\t The Chef’s Kitchen")
        else:
            print("\t Main Street Pizza Company")
            print("\t Corner Café")
            print("\t The Chef’s Kitchen")
    else:
        print("\t Mama’s Fine Italian")
        print("\t Main Street Pizza Company")
        print("\t Corner Café")
        print("\t The Chef’s Kitchen")
else:
    print("\t Joe's Gourmet Burgers")
    print("\t Mama’s Fine Italian")
    print("\t Main Street Pizza Company")
    print("\t Corner Café")
    print("\t The Chef’s Kitchen")

print("")

enter = input ("Press enter to continue")
print("")

print("Question 19 - Turtle Graphics: Hit the Target Modification")
print("Enhance the hit_the_target.py program that you saw in Program 3-9 so \
that, when the projectile misses the target, it displays hints to the user \
indicating whether the angle and/or the force value should be increased or \
decreased. For example, the program should display messages such as 'Try a \
greater angle' and 'Use less force.'")
print("")
# Hit the Target Game 
import turtle
 
# Named constants
SCREEN_WIDTH = 600     # Screen width
SCREEN_HEIGHT = 600    # Screen height
TARGET_LLEFT_X = 100   # Target's lower-left X
TARGET_LLEFT_Y = 250   # Target's lower-left Y
TARGET_WIDTH = 25      # Width of the target
FORCE_FACTOR = 30      # Arbitrary force factor
PROJECTILE_SPEED = 1   # Projectile's animation speed
NORTH = 90             # Angle of north direction
SOUTH = 270            # Angle of south direction
EAST = 0               # Angle of east direction
WEST = 180             # Angle of west direction
 
# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
  
# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()
 
# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)
  
# Get the angle and force from the user.
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1−10): "))
  
# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading.
turtle.setheading(angle)
  
# Launch the projectile.
turtle.pendown()
turtle.forward(distance)
 
# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Target hit!')
else:
    print('You missed the target.')

enter = input ("Press enter to continue")
print("")

print("Thanks for checking out Programming Assignments for Chapter 3! ")
print("Check out some of the other Programming Assignment I have up.")
print("Goodbye!")
