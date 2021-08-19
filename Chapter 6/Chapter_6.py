NUMBER_OF_QUESTIONS = 26

def main ():
    menu()

def print_question(i):
    file_name = "Question " + str(i) + ".txt"
    
    
    input_file = open(file_name, 'r')

    file_contents = input_file.read()
    print(file_contents)

    input_file.close()

    print("-----------------------------------")
 
def get_answer():
    input("Press enter to show the solution")
 
def return_to_menu():
    print("")
    input("Press enter to return to menu")
    menu()
 
def quit_program():
    print("Thank you for checking out Chapter 6 Programming Assignments!")
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
    QUIT_PROGRAM = 13
 
    choice = 0
 
    while (choice != QUIT_PROGRAM):
        print("Here are the questions for chapter 6 - Files and Exceptions")
        print("\t Question Menu")
 
        print("Question 1 - File Display")
        print("Question 2 - File Head Display")
        print("Question 3 - Line Numbers")
        print("Question 4 - Item Counter")
        print("Question 5 - Sum of Numbers")
        print("Question 6 - Average of Numbers")
        print("Question 7 - Random Number File Writer")
        print("Question 8 - Random Number File Reader")
        print("Question 9 - Exception Handing")
        print("Question 10 - Golf Scores")
        print("Question 11 - Personal Web Page Generator")
        print("Question 12 - Average Steps Taken")
 
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
            quit_program()
 
def Question_1():
    print_question(1)
 
    return_to_menu()
 
 
def Question_2():
    print_question(2)
 
    return_to_menu()
 
 
def Question_3():
    print_question(3)
 
    return_to_menu()
    
 
def Question_4():
    print_question(4)
 
    return_to_menu()
 
 
def Question_5():
    print_question(5)
 
    return_to_menu()
 
 
def Question_6():
    print_question(6)
 
    return_to_menu()
   
 
def Question_7():
    print_question(7)
 
    return_to_menu()
 
 
def Question_8():
    print_question(8)
 
    return_to_menu()
 
 
def Question_9():
    print_question(9)
 
    return_to_menu()
      
 
def Question_10():
    print_question(10)
 
    return_to_menu()
  
 
def Question_11():
    print_question(11)
 
    return_to_menu()
 
def Question_12():
    print_question(12)
 
    return_to_menu()
      
main()


