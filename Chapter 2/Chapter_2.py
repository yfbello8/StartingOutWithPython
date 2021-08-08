print("Chapter 2 - Input, Processing, and Output")
print("This programs displays the Programming Challenges in Chapter 2")
print("")

print("Question 1 - Personal Information")
print("Write a program that displays the following information:")
print("")
print("- Your name")
print("- Your address, with city, state, and ZIP")
print("- Your telephone number")
print("- Your college major")
print("")
print("My name is Yusuf. My address is 123 Ryan Terrace, San Ramon, CA, 90332 \n")

enter = input ("Press enter to continue")
print("")

print("Question 2 - Sales Prediction")
print("A company has determined that its annual profit is typically 23 percent \
of total sales. Write a program that asks the user to enter the projected \
amount of total sales, then displays the profit that will be made from that amount.")
print("")
total_sales = float(input("Enter the projected amount of total sales: "))
profit = 1.23 * total_sales 
print("Profit: $", profit)
print("")

enter = input ("Press enter to continue")
print("")

print("Question 3 - Land Calculation")
print("One acre of land is equivalent to 43,560 square feet. Write a program \
that asks the user to enter the total square feet in a tract of land and \
calculates the number of acres in the tract.")
print("")
feet = float(input("Enter the number of square feet you want to convert: "))
acres = feet / 43560.0
print("Numbers of acres:", acres)
print("")

enter = input ("Press enter to continue")
print("")

print("Question 4 - Total Purchase")
print("A customer in a store is purchasing five items. Write a program that \
asks for the price of each item, then displays the subtotal of the sale, the \
amount of sales tax, and the total. Assume the sales tax is 7 percent.")
item_1 = float(input('Enter the price of the first item: '))
item_2 = float(input('Enter the price of the second items: '))
item_3 = float(input('Enter the price of the third items: '))
item_4 = float(input('Enter the price of the fourth items: '))
item_5 = float(input('Enter the price of the fifth items: '))
subtotal = item_1 + item_2 + item_3 + item_4 + item_5
sales_tax = subtotal * .07
total = subtotal * 1.07
print("The subtotal of the five items is $", format(subtotal, ',.2f'), sep='')
print("The sales tax for this purchase is $", format(sales_tax, ',.2f'), sep='')
print("The final total is $", format(total, ',.2f'), sep='')
print("")

enter = input ("Press enter to continue")
print("")

print("Question 5 - Distance Traveled")
print("Assuming there are no accidents or delays, the distance that a car \
travels down the interstate can be calculated with the following formula:")
print("Distance = Speed * Time")
print("A car is traveling at 70 miles per hour. Write a program that displays \
the following:")
print("- The distance the car will travel in 6 hours")
print("- The distance the car will travel in 10 hours")
print("- The distance the car will travel in 15 hours")
print("")
speed = int(70.0)
distance = speed * 6
print("The car will travel", distance, "in 6 hours")
distance = speed * 10
print("The car will travel", distance, "in 10 hours")
distance = speed * 15
print("The car will travel", distance, "in 15 hours")
print("")

enter = input ("Press enter to continue")
print("")

print("Question 6 - Sales Tax")
print("Write a program that will ask the user to enter the amount of a purchase. \
The program should then compute the state and county sales tax. Assume the \
state sales tax is 5 percent and the county sales tax is 2.5 percent. The \
program should display the amount of the purchase, the state sales tax, the \
county sales tax, the total sales tax, and the total of the sale (which is the \
sum of the amount of purchase plus the total sales tax)")
print("Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent \
5 percent.")
print("")
purchase_amount = int(input("Enter the amount of a purchase: "))
state_tax = purchase_amount * 0.05
county_tax = purchase_amount * 0.025
total_tax = state_tax + county_tax
total = purchase_amount  + state_tax + county_tax
print("Purchase Amount:  $", format(purchase_amount, ',.2f'))
print("State Sales Tax:  $", format(state_tax, ',.2f'))
print("County Sales Tax: $", format(county_tax, ',.2f'))
print("Total Sales Tax:  $", format(total_tax, ',.2f'))
print("Purchase Amount:  $", format(total, ',.2f'))
print("")

enter = input ("Press enter to continue")
print("")

print("Question 7 - Miles - per - Gallon")
print("A car's miles-per-gallon (MPG) can be calculated with the following \
formula:")
print("MPG = Miles driven / Gallons of gas used")
print("Write a program that asks the user for the number of miles driven and \
the gallons of gas used. It should calculate the car's MPG and display the \
result")
print("")
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallons used: "))
mpg = miles_driven / gallons_used
print("The MPG of the car is", format(mpg, ',.2f'))
print("")

enter = input ("Press enter to continue")
print("")

print("Question 8 - Tip, Tax, and Total")
print("Write a program that calculates the total amount of a meal purchased at \
a restaurant. The program should ask the user to enter the charge for the food, \
then calculate the amounts of a 18 percent tip and 7 percent sales tax. Display \
each of these amounts and the total.")
print("")
food_charge = float(input("Enter the charge of the food: "))
tip = food_charge * .18
sales_tax = food_charge * .07
total_bill = food_charge + tip + sales_tax 
print("Total charged for food: $", format(food_charge, ',.2f'), sep='')
print("Total tip:              $", format(tip, ',.2f' ), sep='')
print("Total sales tax:        $", format(sales_tax, ',.2f'), sep='')
print("Total bill:             $", format(total_bill, ',.2f'), sep='')
print("")

enter = input ("Press enter to continue")
print("")

print("Question 9 - Celsius to Fahrenheit Temperature Converter")
print("Write a program that converts Celsius temperatures to Fahrenheit \
temperatures. The formula is as follows:")
print("F = 95C + 32")
print("The program should ask the user to enter a temperature in Celsius, then\
display the temperature converted to Fahrenheit")
celsius = float(input("Enter a temperature in Celsius: ")) 
fahrenheit = ((9/5.0) * celsius) + 32 
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
print("")

enter = input ("Press enter to continue")
print("")

print("Question 10 - Ingredient Adjuster")
print("A cookie recipe calls for the following ingredients:")
print("- 1.5 cups of sugar")
print("- 1 cup of butter")
print("- 2.75 cups of flour")
print("The recipe produces 48 cookies with this amount of the ingredients. \
Write a program that asks the user how many cookies he or she wants to make, \
then displays the number of cups of each ingredient needed for the specified \
number of cookies.")
# I chose to do this by getting the amount of cups needed to make 1 cookie
# This is why I divide each entry by 48.0
sugar = 1.5 / 48.0
butter = 1 / 48.0
flour = 2.75 / 48.0
print("")
cookies = int(input("Enter the number of cookies you want to make: "))
sugar = sugar * cookies
butter = butter * cookies
flour = flour * cookies
print("Cups of sugar needed: ", format(sugar, ',.2f'))
print("Cups of butter needed:", format(butter, ',.2f'))
print("Cups of flour needed: ", format(flour, ',.2f'))
print("")

enter = input ("Press enter to continue")
print("")

print("Question 11 - Male and Female Percentages")
print("Write a program that asks the user for the number of males and the \
number of females registered in a class. The program should display the \
percentage of males and females in the class")
print("Hint: Suppose there are 8 males and 12 females in a class. There are 20 \
students in the class. The percentage of males can be calculated as 8 ÷ 20 = \
0.4, or 40%. The percentage of females can be calculated as 12 ÷ 20 = 0.6, or \
60%.")
print("")
males = int(input("Enter the number of males in the class: "))
females = int(input("Enter the number of females in the class: "))
total = males + females
percent_males = (males / total) / 100
percent_females = (females / total) / 100
print("Percent males:", format(percent_males, ',.2%'))
print("Percent females:", format(percent_females,',.2%'))
print("")

enter = input ("Press enter to continue")
print("")

print("Question 12 - Stock Transaction Program")
print("Last month, Joe purchased some stock in Acme Software, Inc. Here are \
the details of the purchase:")
print("- The number of shares that Joe purchased was 2,000")
print("- When Joe purchased the stock, he paid $40.00 per share")
print("- Joe paid his stockbroker a commission that amounted to 3 percent of \
the amount he paid for the stock")
print("Two weeks later, Joe sold the stock. Here are the details of the sale:")
print("- The number of shares that Joe sold was 2,000")
print("- He sold the stock for $42.75 per share")
print("- He paid his stockbroker another commission that amounted to 3 percent \
of the amount he received for the stock")
print("- The amount of money Joe paid for the stock")
print("- The amount of commission Joe paid his broker when he bought the stock")
print("- The amount for which Joe sold the stock")
print("- The amount of commission Joe paid his broker when he sold the stock")
print("- Display the amount of money that Joe had left when he sold the stock \
and paid his broker (both times). If this amount is positive, then Joe made a \
profit. If the amount is negative, then Joe lost money")
print("")
amount_stock = 2000
amount_paid = amount_stock * 40
buying_stockbroker_cost = amount_paid * 0.03
amount_received = amount_stock * 42.75
selling_stockbroker_cost = amount_received * 0.03
net = (amount_received - selling_stockbroker_cost) - (amount_paid + \
    buying_stockbroker_cost)
print("Amount paid to buy stock:                $", \
    format(amount_paid, ',.2f'), sep='')
print("Amount paid to stockbroker when buying:  $", \
    format(buying_stockbroker_cost, ',.2f'), sep='')
print("Amount earned from selling stock:        $", \
    format(amount_received, ',.2f'), sep='')
print("Amount paid to stockbroker when selling: $", \
    format(selling_stockbroker_cost, ',.2f'), sep='')
print("Net profit or loss:                      $", format(net, ',.2f'), sep='')
print("")

enter = input ("Press enter to continue")
print("")

print("Question 13 - Planting Grapevines")
print("A vineyard owner is planting several new rows of grapevines, and needs \
to know how many grapevines to plant in each row. She has determined that \
after measuring the length of a future row, she can use the following formula \
to calculate the number of vines that will fit in the row, along with the \
trellis end-post assemblies that will need to be constructed at each end of \
the row:")
print("V = (R - 2E)/S")
print("The terms in the formula are:")
print("- V is the number of grapevines that will fit in the row")
print("- R is the length of the row, in feet")
print("- E is the amount of space, in feet, used by an end-post assembly")
print("- S is the space between vines, in feet")
print("Write a program that makes the calculation for the vineyard owner. \
The program should ask the user to input the following:")
print("- The length of the row, in feet")
print("- The amount of space used by an end-post assembly, in feet")
print("- The amount of space between the vines, in feet")
print("Once the input data has been entered, the program should calculate and \
display the number of grapevines that will fit in the row")
print("")
row_length = float(input("Enter the row length, in feet: "))
end_post_assebly_space = float(input("Enter the space used by an end-post \
assembly, in feet: "))
space_between_vines = float(input("Enter the space between the vines: "))
num_grapevines = (row_length - (2*end_post_assebly_space*space_between_vines))\
   / space_between_vines
print("The number of grapevines that will fit in the row is", \
    format(num_grapevines, ',.2f'))
print("")

enter = input ("Press enter to continue")
print("")

print("Question 14 - Compound Interest")
print("When a bank account pays compound interest, it pays interest not only on\
the principal amount that was deposited into the account, but also on the \
interest that has accumulated over time. Suppose you want to deposit some \
money into a savings account, and let the account earn compound interest for a \
certain number of years. The formula for calculating the balance of the \
account after a specified number of years is:")
print("A = P * (1 + r/n)^(n*t)")
print("The terms in the formula are:")
print("- A is the amount of money in the account after the specified number of years")
print("- P is the principal amount that was originally deposited into the account")
print("- r is the annual interest rate")
print("- n is the number of times per year that the interest is compounded")
print("- t is the specified number of years")
print("Write a program that makes the calculation for you. The program should \
ask the user to input the following:")
print("The amount of principal originally deposited into the account")
print("The annual interest rate paid by the account")
print("The number of times per year that the interest is compounded (For \
example, if interest is compounded monthly, enter 12. If interest is compounded\
quarterly, enter 4.)")
print("The number of years the account will be left to earn interest")
print("Once the input data has been entered, the program should calculate and \
display the amount of money that will be in the account after the specified \
number of years")
print("Note: The user should enter the interest rate as a percentage. For \
example, 2 percent would be entered as 2, not as .02. The program will then \
have to divide the input by 100 to move the decimal point to the correct \
position.")
print("")
principal = float(input("Enter the principal amount that was originally \
deposited into the account: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
annual_interest_rate = annual_interest_rate / 100.0
compounding_num = float(input("Enter the number of times per year that the \
interest is compounded (For example, if interest is compounded monthly,\
enter 12. If interest is compounded quarterly, enter 4.): "))
num_years = float(input("Enter the number of years the account will be left to \
earn interest: "))

# There was an issue with the math so I decided to debug just the math aspect of it
#print("P = ", principal)
#print("r = ", annual_interest_rate)
#print("n = ", compounding_num)
#print("t = ", num_years)
#print("")
#print("r/n = ", annual_interest_rate / compounding_num)
#print("(r/n)**(n*t)", ((annual_interest_rate / compounding_num) ** (compounding_num * num_years)))
#

final_amount = principal * ((1 + (annual_interest_rate/compounding_num))**\
    (compounding_num*num_years))
print("After", num_years, "years, the money in the account would have grown to $",\
    format(final_amount, ',.2f'))
print("")

enter = input ("Press enter to continue")
print("")

print("Question 15 - Turtle Graphics Drawings")
print("Use the turtle graphics library to write programs that reproduce each \
of the designs shown in Figure 2-34")
print("")
# I have only done 1 of the 6 designs now. I will do the rest later
import turtle
turtle.speed(1)
# Begin creating the first shape
turtle.bgcolor('gray')
turtle.fillcolor('white')
turtle.begin_fill()
turtle.showturtle()
turtle.setheading(45)
turtle.forward(100)
turtle.setheading(-45)
turtle.forward(100)
turtle.setheading(225)
turtle.forward(100)
turtle.setheading(135)
# End the first shape and begin the second shape
turtle.forward(200)
turtle.setheading(225)
turtle.forward(100)
turtle.setheading(-45)
turtle.forward(100)
turtle.setheading(45)
turtle.forward(100)
turtle.end_fill()
turtle.reset()


enter = input ("Press enter to continue")
print("")
