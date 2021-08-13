print("Chapter 4 - Repetition Structures")
print("This program displays the Programming Challenges in Chapter 4")
print("")

enter = input ("Press enter to continue")
print("")




print("Question 1 - Bug Collector")
print("A bug collector collects bugs every day for five days. Write a program \
that keeps a running total of the number of bugs collected during the five \
days. The loop should ask for the number of bugs collected for each day, and \
when the loop is finished, the program should display the total number of \
bugs collected")
print("")
running_bug_count = 0

for day in [1,2,3,4,5]:
    daily_bug_count = int(input("Enter the number of bugs collected on day " \
        + str(day) + ": "))
    running_bug_count += daily_bug_count

# Initially I misunderstood the question and wanted to try and push myself a 
# little bit to make the code a little more complex. I was having errors but 
# as a result, rediscovered string concatenation 
#for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", \
#   "Sunday"]:
#    daily_bug_count = int(input("Enter the number of bugs collected on day ", \
#    day, ": "))
#    running_bug_count += daily_bug_count

print("The number of bugs collected over 5 days:", running_bug_count)
print("")

enter = input ("Press enter to continue")
print("")

print("Question 2 - Calories Burned")
print("Running on a particular treadmill you burn 4.2 calories per minute. \
Write a program that uses a loop to display the number of calories burned \
after 10, 15, 20, 25, and 30 minutes")
print("")
print("Minutes \t Calories Burned")
for minutes in (10, 15, 20, 25, 30):
    print(minutes, "\t", minutes*4.2)
print("")

enter = input ("Press enter to continue")

print("")

print("Question 3 - Budget Analysis")
print("Write a program that asks the user to enter the amount that he or she \
has budgeted for a month. A loop should then prompt the user to enter each of \
his or her expenses for the month and keep a running total. When the loop \
finishes, the program should display the amount that the user is over or \
under budget")
print("")
amount_budgeted = float(input("Enter the amount budgeted for the month: "))
expense = 0

while expense != 0:
    expense = float(input("Enter an expense amount"))
    total_expense += expense

# Calculate the if the total expense is over or under budget 
if total_expense > amount_budgeted:
    print("You were over budget by $", (total_expense - amount_budgeted))
elif total_expense < amount_budgeted:
    print("You were under budget by $", (amount_budgeted - total_expense))
else:
    print("You met your budget perfectly!")

print("")

enter = input ("Press enter to continue")
print("")

print("Question 4 - Distance Traveled")
print("The distance a vehicle travels can be calculated as follows:")
print("")
print("distance = speed * time")
print("")
print("For example, if a train travels 40 miles per hour for three hours, \
the distance traveled is 120 miles. Write a program that asks the user for \
the speed of a vehicle (in miles per hour) and the number of hours it has \
traveled. It should then use a loop to display the distance the vehicle has \
traveled for each hour of that time period. Here is an example of the desired \
output")
print("")
print("What is the speed of the vehicle in mph? 40 [ENTER]")
print("How many hours has it traveled? 3 [ENTER]")
print("")
print("Hours \t\t Distance Traveled")
print("")
print("1 \t\t 40")
print("2 \t\t 80")
print("3 \t\t 120")
print("")
speed = float(input("Enter the speed of a vehicle (in miles per hour): "))
hours_traveled = int(input("Enter the number of hours the vehicle has traveled: "))
print("Hours \t\t Distance Traveled")
print("")

for hours in range (1,hours_traveled+1):
    print(hours, "\t\t", hours*speed) 

print("")

enter = input ("Press enter to continue")
print("")

print("Question 5 - Average Rainfall")
print("Write a program that uses nested loops to collect data and calculate \
the average rainfall over a period of years. The program should first ask for \
the number of years. The outer loop will iterate once for each year. The inner \
loop will iterate twelve times, once for each month. Each iteration of the \
inner loop will ask the user for the inches of rainfall for that month. After \
all iterations, the program should display the number of months, the total \
inches of rainfall, and the average rainfall per month for the entire period")
print("")
total_inches = 0

num_years = int(input("Enter the number of years: "))
for year in range (1, num_years+1):
    for month in range (1,13):
        inches = float(input("Enter the inches of rain that fell in month " + str(month) + ": "))
        total_inches += inches
print("Total number of months:", num_years*12)
print("Total inches of rainfall:", total_inches)
print("Average rainfall per month:", total_inches/(num_years*12))
print("")

enter = input ("Press enter to continue")
print("")

print("Question 6 - Celsius to Fahrenheit Table")
print("Write a program that displays a table of the Celsius temperatures 0 \
through 20 and their Fahrenheit equivalents. The formula for converting a \
temperature from Celsius to Fahrenheit is")
print("")
print("F = (9/5) * C + 32")
print("")
print("where F is the Fahrenheit temperature, and C is the Celsius \
temperature. Your program must use a loop to display the table")
print("")
print("Fahrenheit \t Celsius")

for temp in range (0,21):
    print(temp, "\t\t", ((9/5)*temp)+32)
print("")

enter = input ("Press enter to continue")
print("")

print("Question 7 - Pennies for Pay")
print("Write a program that calculates the amount of money a person would \
earn over a period of time if his or her salary is one penny the first day, \
two pennies the second day, and continues to double each day. The program \
should ask the user for the number of days. Display a table showing what the \
salary was for each day, then show the total pay at the end of the period. \
The output should be displayed in a dollar amount, not the number of pennies")
print("")
num_days = int(input("Enter the number of days: "))
dollars = .01
total_pay = 0
print("Days \t\t Pay (in dollars)")
#print(1, "\t\t", .01)
for days in range (1,num_days+1):
    
    print(days, "\t\t", format(dollars, ',.2f'))
    dollars +=dollars
    total_pay+= dollars
print("Total Pay:", format(total_pay, ',.2f'))

enter = input ("Press enter to continue")
print("")

print("Question 8 - Sum of Numbers")
print("Write a program with a loop that asks the user to enter a series of \
positive numbers. The user should enter a negative number to signal the end \
of the series. After all the positive numbers have been entered, the program \
should display their sum")
print("")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 9 - Ocean Levels")
print("Assuming the ocean’s level is currently rising at about 1.6 millimeters \
per year, create an application that displays the number of millimeters that \
the ocean will have risen each year for the next 25 years")
print("")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 10 - Tuition Increase")
print("At one college, the tuition for a full-time student is $8,000 per \
semester. It has been announced that the tuition will increase by 3 \
percent each year for the next 5 years. Write a program with a loop that \
displays the projected semester tuition amount for the next 5 years")
print("")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 11 - Weight Loss")
print("If a moderately active person cuts their calorie intake by 500 \
calories a day, they can typically lose about 4 pounds a month. Write a \
program that lets the user enter their starting weight, then creates and \
displays a table showing what their expected weight will be at the end of \
each month for the next 6 months if they stay on this diet")
print("")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 12 - Calculating the Factorial of a Number")
print("In mathematics, the notation n! represents the factorial of the \
nonnegative integer n. The factorial of n is the product of all the \
nonnegative integers from 1 to n. For example.")
print("")
print("7! = 1 * 2 * 3 * 4 * 5 * 6 * 7 = 5,040")
print("and")
print("4! = 1 * 2 * 3 * 4 = 24")
print("Write a program that lets the user enter a nonnegative integer then \
uses a loop to calculate the factorial of that number. Display the factorial")
print("")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 13 - Population")
print("Write a program that predicts the approximate size of a population of \
organisms. The application should use text boxes to allow the user to enter \
the starting number of organisms, the average daily population increase \
(as a percentage), and the number of days the organisms will be left to \
multiply. For example, assume the user enters the following values:")
print("")
print("Starting number of organisms: 2")
print("Average daily increase: 30%")
print("Number of days to multiply: 10")
print("")
print("The program should display the following table of data:")
print("")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 14 - Write a program that uses nested loops to draw this pattern:")
print("*******")
print("******")
print("*****")
print("****")
print("***")
print("**")
print("*")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 15 - Write a program that uses nested loops to draw this pattern:")
print("##")
print("# #")
print("#  #")
print("#   #")
print("#    #")
print("#     #")
print("")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 16 - Turtle Graphics: Repeating Squares")
print("In this chapter, you saw an example of a loop that draws a square. \
Write a turtle graphics program that uses nested loops to draw 100 squares, \
to create the design shown in Figure 4-13.")
print("")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 17 - Turtle Graphics: Star Pattern")
print("Use a loop with the turtle graphics library to draw the design shown \
in Figure 4-14")
print("")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 18 - Turtle Graphics: Hypnotic Pattern")
print("Use a loop with the turtle graphics library to draw the design shown in \
Figure 4-15")
print("")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 19 - Turtle Graphics: STOP Sign")
print("In this chapter, you saw an example of a loop that draws an octagon. \
Write a program that uses the loop to draw an octagon with the word “STOP” \
displayed in its center. The STOP sign should be centered in the graphics window")
print("")
print("")
print("")
print("")

enter = input ("Press enter to continue")
print("")


print("Thanks for checking out Programming Assignments for Chapter 4! ")
print("Check out some of the other Programming Assignment I have up.")
print("Goodbye!")

