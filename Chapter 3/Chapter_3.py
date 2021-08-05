print("Chapter 3 - Decision Structures and Boolean Logic")
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
    print("3")
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
print("")
print("")
print("")
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
print("")
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
print("")
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
print("")
print("")
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
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 12 - Software Sales")
print("A software company sells a package that retails for $99. Quantity \
discounts are given according to the following table:")
print("")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 13 - ")
print("")
print("")
print("")
print("")
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
print("")

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
print("")
print("")
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
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")
