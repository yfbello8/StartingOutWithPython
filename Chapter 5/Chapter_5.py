def main ():
    menu()

def get_answer():
    input("Press enter to show the solution")

def return_to_menu():
    input("Press enter to return to menu")
    menu()

def quit_program():
    print("Thank you for checking out Chapter 5 Programming Assignments!")
    print("Please let me know your thoughts and suggestions! Check out other \
    chapters as well! See you later!")

def menu():
    QUESTION_1 = 1
    QUESTION_2 = 2
    QUESTION_3 = 3
    QUESTION_4 = 4
    QUESTION_5 = 5
    QUESTION_6 = 6
    QUESTION_7 = 7
    QUESTION_8 = 8
    QUESTION_9 = 9
    QUESTION_10 = 10
    QUESTION_11 = 11
    QUESTION_12 = 12
    QUESTION_13 = 13
    QUESTION_14 = 14
    QUESTION_15 = 15
    QUESTION_16 = 16
    QUESTION_17 = 17
    QUESTION_18 = 18
    QUESTION_19 = 19
    QUESTION_20 = 20
    QUESTION_21 = 21
    QUESTION_22 = 22
    QUESTION_23 = 23
    QUESTION_24 = 24
    QUESTION_25 = 25
    QUESTION_26 = 26
    QUIT_PROGRAM = 27

    choice = 0

    while (choice != QUIT_PROGRAM):
        print("Here are the questions for chapter 5 - Functions")
        print("\t Question Menu")

        print("Question 1 - Kilometer Converter")
        print("Question 2 - Sales Tax Program Refactoring")
        print("Question 3 - How Much Insurance?")
        print("Question 4 - Automobile Costs")
        print("Question 5 - Property Tax")
        print("Question 6 - Calories from Fat and Carbohydrates")
        print("Question 7 - Stadium Seating")
        print("Question 8 - Paint Job Estimator")
        print("Question 9 - Monthly Sales Tax")
        print("Question 10 - Feet to Inches")
        print("Question 11 - Math Quiz")
        print("Question 12 - Maximum of Two Values")
        print("Question 13 - Falling Distance")
        print("Question 14 - Kinetic Energy")
        print("Question 15 - Test Average and Grade")
        print("Question 16 - Odd/Even Counter")
        print("Question 17 - Prime Numbers")
        print("Question 18 - Prime Number List")
        print("Question 19 - Future Value")
        print("Question 20 - Random Number Guessing Game")
        print("Question 21 - Rock, Paper, Scissors Game")
        print("Question 22 - Turtle Graphics: Triangle Function")
        print("Question 23 - Turtle Graphics: Modular Snowman")
        print("Question 24 - Turtle Graphics: Rectangular Pattern")
        print("Question 25 - Turtle Graphics: Checkerboard")
        print("Question 26 - Turtle Graphics: City Skyline")

        choice = int(input("What question do you want to look at? "))
        print("")

        while (choice < 0 and choice > QUIT_PROGRAM):
            print("ERROR! Wrong selection")
            choice = int(input("Please enter a valid choice: "))

        if choice == 1:
            Question_1()
        elif choice == 2:
            Question_2()
        elif choice == 3:
            Question_3()
        elif choice == 4:
            Question_4()
        elif choice == 5:
            Question_5()
        elif choice == 6:
            Question_6()
        elif choice == 7:
            Question_7()
        elif choice == 8:
            Question_8()
        elif choice == 9:
            Question_9()
        elif choice == 10:
            Question_10()
        elif choice == 11:
            Question_11()
        elif choice == 12:
            Question_12()
        elif choice == 13:
            Question_13()
        elif choice == 14:
            Question_14()
        elif choice == 15:
            Question_15()
        elif choice == 16:
            Question_16()
        elif choice == 17:
            Question_17()
        elif choice == 18:
            Question_18()
        elif choice == 19:
            Question_19()
        elif choice == 20:
            Question_20()
        elif choice == 21:
            Question_21()
        elif choice == 22:
            Question_22()
        elif choice == 23:
            Question_23()
        elif choice == 24:
            Question_24()
        elif choice == 25:
            Question_25()
        elif choice == 26:
            Question_26()
        elif choice == 27:
            quit_program()

def km_to_miles(km):
    return km * 0.6214

def Question_1():
    print("Question 1 - Kilometer Converter")
    print("Write a program that asks the user to enter a distance in kilometers, \
    then converts that distance to miles. The conversion formula is as follows:")
    print("")
    print("Miles = Kilometers * 0.6214")
    print("")
    km = float(input("Enter a distance in kilometers to be converted to miles: "))
    print(km_to_miles(km), "miles")
    print("")

    return_to_menu()

def display_final_price(final_price):
    print("Final price is $", final_price, sep='')
 
def tax_calculator(list_price):
    state_tax = list_price * .05
    county_tax = list_price * .025
    final_price = list_price + state_tax + county_tax
    display_final_price(final_price)
    

def Question_2():
    print("Question 2 - Sales Tax Program Refactoring")
    print("Programming Exercise #6 in Chapter 2 was the Sales Tax program. For \
    that exercise, you were asked to write a program that calculates and \
    displays the county and state sales tax on a purchase. If you have already \
    written that program, redesign it so the subtasks are in functions. If you \
    have not already written that program, write it using functions")
    print("")
    list_price = float(input("Enter the list price of the item: "))
    tax_calculator(list_price)
    print("")

    return_to_menu()

def building_insurance(building_cost):
    return building_cost * 0.8

def Question_3():
    print("Question 3 - How Much Insurance?")
    print("Many financial experts advise that property owners should insure \
    their homes or buildings for at least 80 percent of the amount it would \
    cost to replace the structure. Write a program that asks the user to enter \
    the replacement cost of a building, then displays the minimum amount of \
    insurance he or she should buy for the property")
    print("")
    building_cost = float(input("Enter the cost of the building: "))
    print("Minimal amount of insurance you should purchase: $", \
        building_insurance(building_cost), sep='')
    print("")

    return_to_menu()
    
def annual_cost(expense):
    return expense*12

def Question_4():
    print("Question 4 - Automobile Costs")
    print("Write a program that asks the user to enter the monthly costs for \
    the following expenses incurred from operating his or her automobile: loan \
    payment, insurance, gas, oil, tires, and maintenance. The program should \
    then display the total monthly cost of these expenses, and the total annual \
    cost of these expenses")
    print("")
    loan = float(input("Enter your monthly loan payment: "))
    insurance = float(input("Enter your monthly insurance payment: "))
    gas = float(input("Enter your monthly gas payment: "))
    oil = float(input("Enter your monthly oil payment: "))
    tires = float(input("Enter your monthly tires payment: "))
    maintenance = float(input("Enter your monthly maintenance payment: "))
    print("Expense \t\t Annual Cost")
    print("Loan Payment \t\t $", annual_cost(loan), sep='')
    print("Insurance \t\t $", annual_cost(insurance), sep='')
    print("Gas \t\t\t $", annual_cost(gas), sep='')
    print("Oil \t\t\t $", annual_cost(oil), sep='')
    print("Tires \t\t\t $", annual_cost(tires), sep='')
    print("Maintenance \t\t $", annual_cost(maintenance), sep='')
    print("")

    return_to_menu()

def property_tax_calculator(assessment_value):
    property_tax = (assessment_value / 100) * .72
    print("Assessment value: $", assessment_value, sep='')
    print("Property tax: $", format(property_tax,',.2f'), sep='')

def assessment_value_calculator(actual_value):
    assessment_value = actual_value * 0.6
    property_tax_calculator(assessment_value)

def Question_5():
    print("Question 5 - Property Tax")
    print("A county collects property taxes on the assessment value of \
    property, which is 60 percent of the property’s actual value. \
    For example, if an acre of land is valued at $10,000, its assessment value \
    is $6,000. The property tax is then 72¢ for each $100 of the assessment \
    value. The tax for the acre assessed at $6,000 will be $43.20. Write a \
    program that asks for the actual value of a piece of property and displays \
    the assessment value and property tax")
    print("")
    actual_value = float(input("Enter the actual value of the property: "))
    assessment_value_calculator(actual_value)
    print("")

    return_to_menu()

def calories_from_carbs(carb_grams):
    return carb_grams * 4

def calories_from_fat(fat_grams):
    return fat_grams * 9

def Question_6():
    print("Question 6 - Calories from Fat and Carbohydrates")
    print("A nutritionist who works for a fitness club helps members by \
    evaluating their diets. As part of her evaluation, she asks members for \
    the number of fat grams and carbohydrate grams that they consumed in a \
    day. Then, she calculates the number of calories that result from the fat, \
    using the following formula:")
    print("")
    print("calories from fat = fat grams * 9")
    print("")
    print("Next, she calculates the number of calories that result from the \
    carbohydrates, using the following formula:")
    print("calories from carbs = carb grams * 4")
    print("")
    print("The nutritionist asks you to write a program that will make these \
    calculations")
    print("")
    fat_grams = float(input("Enter the number of fat grams consumed in a day: "))
    carb_grams = float(input("Enter the number of carb grams consumed in a day: "))

    print("Calories from fat:", calories_from_fat(fat_grams))
    print("Calories from carbs:", calories_from_carbs(carb_grams))
    return_to_menu()
   

def Question_7():
    print("Question 7 - Stadium Seating")
    print("There are three seating categories at a stadium. Class A seats \
    cost $20, Class B seats cost $15, and Class C seats cost $10. Write a \
    program that asks how many tickets for each class of seats were sold, \
    then displays the amount of income generated from ticket sales")
    print("")
    class_a_tickets_sold = int(input("Enter the number of Class A tickets sold: "))
    class_b_tickets_sold = int(input("Enter the number of Class B tickets sold: "))
    class_c_tickets_sold = int(input("Enter the number of Class C tickets sold: "))
    
    class_a_ticket_sales(class_a_tickets_sold)
    class_b_ticket_sales(class_b_tickets_sold)
    class_c_ticket_sales(class_c_tickets_sold)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    return_to_menu()


def Question_8():
    print("Question 8 - Paint Job Estimator")
    print("A painting company has determined that for every 112 square feet \
    of wall space, one gallon of paint and eight hours of labor will be \
    required. The company charges $35.00 per hour for labor. Write a program \
    that asks the user to enter the square feet of wall space to be painted \
    and the price of the paint per gallon. The program should display the \
    following data:")
    print("")
    print("- The number of gallons of paint required")
    print("- The hours of labor required")
    print("- The cost of the paint")
    print("- The labor charges")
    print("- The total cost of the paint job")
    print("")

    return_to_menu()


def Question_9():
    print("Question 9 - Monthly Sales Tax")
    print("A retail company must file a monthly sales tax report listing the \
    total sales for the month, and the amount of state and county sales tax \
    collected. The state sales tax rate is 5 percent and the county sales tax \
    rate is 2.5 percent. Write a program that asks the user to enter the total \
    sales for the month. From this figure, the application should calculate \
    and display the following:")
    print("")
    print("- The amount of county sales tax")
    print("- The amount of state sales tax")
    print("- The total sales tax (county plus state)")
    print("")
    print("")
    print("")

    return_to_menu()
      

def Question_10():
    print("Question 10 - Feet to Inches")
    print("One foot equals 12 inches. Write a function named feet_to_inches \
    that accepts a number of feet as an argument and returns the number of \
    inches in that many feet. Use the function in a program that prompts the \
    user to enter a number of feet then displays the number of inches in that \
    many feet")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    return_to_menu()
  

def Question_11():
    print("Question 11 - Math Quiz")
    print("Write a program that gives simple math quizzes. The program should \
    display two random numbers that are to be added, such as:")
    print("")
    print("247 + 129")
    print("")
    print("The program should allow the student to enter the answer. If the \
    answer is correct, a message of congratulations should be displayed. If \
    the answer is incorrect, a message showing the correct answer should be \
    displayed")
    print("")
    print("")
    print("")

    return_to_menu()

def Question_12():
    print("Question 12 - Maximum of Two Values")
    print("Write a function named max that accepts two integer values as \
    arguments and returns the value that is the greater of the two. For \
    example, if 7 and 12 are passed as arguments to the function, the function \
    should return 12. Use the function in a program that prompts the user to \
    enter two integer values. The program should display the value that is the \
    greater of the two")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    return_to_menu()
     

def Question_13():
    print("Question 13 - Falling Distance")
    print("When an object is falling because of gravity, the following formula \
    can be used to determine the distance the object falls in a specific time \
    period:")
    print("")
    print("d = (1/2) * g * t ^2")
    print("")
    print("The variables in the formula are as follows: d is the distance in \
    meters, g is 9.8, and t is the amount of time, in seconds, that the object \
    has been falling")
    print("Write a function named falling_distance that accepts an object’s \
    falling time (in seconds) as an argument. The function should return the \
    distance, in meters, that the object has fallen during that time interval.\
    Write a program that calls the function in a loop that passes the values 1 \
    through 10 as arguments and displays the return value")
    print("")
    print("")

    return_to_menu()

def Question_14():
    print("Question 14 - Kinetic Energy")
    print("In physics, an object that is in motion is said to have kinetic \
    energy. The following formula can be used to determine a moving object’s \
    kinetic energy:")
    print("")
    print("KE = (1/2) * m * v ^2")
    print("The variables in the formula are as follows: KE is the kinetic \
    energy, m is the object’s mass in kilograms, and v is the object’s \
    velocity in meters per second")
    print("Write a function named kinetic_energy that accepts an object’s \
    mass (in kilograms) and velocity (in meters per second) as arguments. \
    The function should return the amount of kinetic energy that the object \
    has. Write a program that asks the user to enter values for mass and \
    velocity, then calls the kinetic_energy function to get the object’s \
    kinetic energy")
    print("")
    print("")
    print("")

    return_to_menu()
    

def Question_15():
    print("Question 15 - Test Average and Grade")
    print("Write a program that asks the user to enter five test scores. \
    The program should display a letter grade for each score and the average \
    test score. Write the following functions in the program:")
    print("- calc_average. This function should accept five test scores as \
    arguments and return the average of the scores")
    print("- determine_grade. This function should accept a test score as an \
    argument and return a letter grade for the score based on the following \
    grading scale:")
    print("Score \t\t Letter Grade")
    print("90-100 \t\t A")
    print("80-89 \t\t B")
    print("70-79 \t\t C")
    print("60-69 \t\t D")
    print("Below 60 \t\t F")

    return_to_menu()
    

def Question_16():
    print("Question 16 - Odd/Even Counter")
    print("In this chapter, you saw an example of how to write an algorithm \
    that determines whether a number is even or odd. Write a program that \
    generates 100 random numbers and keeps a count of how many of those random \
    numbers are even, and how many of them are odd")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    return_to_menu()
       

def Question_17():
    print("Question 17 - Prime Numbers")
    print("A prime number is a number that is only evenly divisible by itself \
    and 1. For example, the number 5 is prime because it can only be evenly \
    divided by 1 and 5. The number 6, however, is not prime because it can be \
    divided evenly by 1, 2, 3, and 6")
    print("Write a Boolean function named is_prime which takes an integer as \
    an argument and returns true if the argument is a prime number, or false \
    otherwise. Use the function in a program that prompts the user to enter a \
    number then displays a message indicating whether the number is prime")
    print("")
    print("Tip: Recall that the % operator divides one number by another and \
    returns the remainder of the division. In an expression such as num1 % \
    num2, the % operator will return 0 if num1 is evenly divisible by num2")
    print("")
    print("")
    print("")
    print("")

    return_to_menu()


def Question_18():
    print("Question 18 - Prime Number List")
    print("This exercise assumes that you have already written the is_prime \
    function in Programming Exercise 17. Write another program that displays \
    all of the prime numbers from 1 to 100. The program should have a loop \
    that calls the is_prime function")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    return_to_menu()


def Question_19():
    print("Question 19 - Future Value")
    print("Suppose you have a certain amount of money in a savings account \
    that earns compound monthly interest, and you want to calculate the \
    amount that you will have after a specific number of months. The \
    formula is as follows:")
    print("")
    print("F = P * (1 + i)^t")
    print("")
    print("The terms in the formula are:")
    print("")
    print("- F is the future value of the account after the specified time period")
    print("- P is the present value of the account")
    print("- i is the monthly interest rate")
    print("- t is the number of months")
    print("")
    print("Write a program that prompts the user to enter the account’s \
    present value, monthly interest rate, and the number of months that the \
    money will be left in the account. The program should pass these values \
    to a function that returns the future value of the account, after the \
    specified number of months. The program should display the account’s \
    future value")
    print("")
    print("")

    return_to_menu()


def Question_20():
    print("Question 20 - Random Number Guessing Game")
    print("Write a program that generates a random number in the range of 1 \
    through 100, and asks the user to guess what the number is. If the user’s \
    guess is higher than the random number, the program should display \
    “Too high, try again.” If the user’s guess is lower than the random \
    number, the program should display “Too low, try again.” If the user \
    guesses the number, the application should congratulate the user and \
    generate a new random number so the game can start over")
    print("")
    print("Optional Enhancement: Enhance the game so it keeps count of the \
    number of guesses that the user makes. When the user correctly guesses the \
    random number, the program should display the number of guesses")
    print("")
    print("")
    print("")
    print("")
    print("")

    return_to_menu()
    

def Question_21():
    print("Question 21 - Rock, Paper, Scissors Game")
    print("Write a program that lets the user play the game of Rock, Paper, \
    Scissors against the computer. The program should work as follows:")
    print("")
    print("1. When the program begins, a random number in the range of 1 \
    through 3 is generated. If the number is 1, then the computer has chosen \
    rock. If the number is 2, then the computer has chosen paper. If the \
    number is 3, then the computer has chosen scissors. (Don’t display the \
    computer’s choice yet.)")
    print("2. The user enters his or her choice of “rock,” “paper,” or \
    “scissors” at the keyboard")
    print("3. The computer’s choice is displayed")
    print("4. A winner is selected according to the following rules:")
    print(" - If one player chooses rock and the other player chooses scissors, \
    then rock wins. (Rock smashes scissors.)")
    print("- If one player chooses scissors and the other player chooses paper, \
    then scissors wins. (Scissors cuts paper.)")
    print("If one player chooses paper and the other player chooses rock, then \
    paper wins. (Paper wraps rock.)")
    print("- If both players make the same choice, the game must be played \
    again to determine the winner")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    return_to_menu()
 

def Question_22():
    print("Question 22 - Turtle Graphics: Triangle Function")
    print("Write a function named triangle that uses the turtle graphics \
    library to draw a triangle. The functions should take arguments for the X \
    and Y coordinates of the triangle’s vertices, and the color with which the \
    triangle should be filled. Demonstrate the function in a program")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    return_to_menu()
      

def Question_23():
    print("Question 23 - Turtle Graphics: Modular Snowman")
    print("Write a program that uses turtle graphics to display a snowman, \
    similar to the one shown in Figure 5-30. In addition to a main function, \
    the program should also have the following functions:")
    print("")
    print("- drawBase. This function should draw the base of the snowman, \
    which is the large snowball at the bottom")
    print("- drawMidSection. This function should draw the middle snowball")
    print("- drawArms. This function should draw the snowman’s arms")
    print("- drawHead. This function should draw the snowman’s head, with \
    eyes, mouth, and other facial features you desire")
    print("- drawHat. This function should draw the snowman’s hat")
    print("")

    return_to_menu()
       

def Question_24():
    print("Question 24 - Turtle Graphics: Rectangular Pattern")
    print("In a program, write a function named drawPattern that uses the \
    turtle graphics library to draw the rectangular pattern shown in Figure \
    5-31. The drawPattern function should accept two arguments: one that \
    specifies the pattern’s width, and another that specifies the pattern’s \
    height. (The example shown in Figure 5-31 shows how the pattern would \
    appear when the width and the height are the same.) When the program runs, \
    the program should ask the user for the width and height of the pattern, \
    then pass these values as arguments to the drawPattern function")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    return_to_menu()
    

def Question_25():
    print("Question 25 - Turtle Graphics: Checkerboard")
    print("Write a turtle graphics program that uses the square function \
    presented in this chapter, along with a loop (or loops) to draw the \
    checkerboard pattern shown in Figure 5-32.")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    return_to_menu()
   

def Question_26():
    print("Question 26 - Turtle Graphics: City Skyline")
    print("Write a turtle graphics program that draws a city skyline similar \
    to the one shown in Figure 5-33. The program’s overall task is to draw an \
    outline of some city buildings against a night sky. Modularize the program \
    by writing functions that perform the following tasks:")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    return_to_menu()

main()
