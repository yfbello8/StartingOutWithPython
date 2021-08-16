def main ():
    menu()

def get_answer():
    input("Press enter to show the solution")

def return_to_menu():
    input("Press enter to return to menu")
    menu()

def quit_program():
    print("Thank you for checking out Chapter XXX Programming Assignments!")
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
        print("Here are the questions for chapter XXX - XXXX")
        print("\t Question Menu")

        print("Question 1 - ")
        print("Question 2 - ")
        print("Question 3 - ")
        print("Question 4 - ")
        print("Question 5 - ")
        print("Question 6 - ")
        print("Question 7 - ")
        print("Question 8 - ")
        print("Question 9 - ")
        print("Question 10 - ")
        print("Question 11 - ")
        print("Question 12 - ")
        print("Question 13 - ")
        print("Question 14 - ")
        print("Question 15 - ")
        print("Question 16 - ")
        print("Question 17 - ")
        print("Question 18 - ")
        print("Question 19 - ")
        print("Question 20 - ")
        print("Question 21 - ")
        print("Question 22 - ")
        print("Question 23 - ")
        print("Question 24 - ")
        print("Question 25 - ")
        print("Question 26 - ")

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

def Question_1():
    print("Question 1 - ")

    return_to_menu()
 

def Question_2():
    print("Question 2 - ")

    return_to_menu()


def Question_3():
    print("Question 3 - ")

    return_to_menu()
    

def Question_4():
    print("Question 4 - ")

    return_to_menu()


def Question_5():
    print("Question 5 - ")

    return_to_menu()


def Question_6():
    print("Question 6 - ")

    return_to_menu()
   

def Question_7():
    print("Question 7 - ")

    return_to_menu()


def Question_8():
    print("Question 8 - ")

    return_to_menu()


def Question_9():
    print("Question 9 - ")

    return_to_menu()
      

def Question_10():
    print("Question 10 - ")

    return_to_menu()
  

def Question_11():
    print("Question 11 - ")

    return_to_menu()

def Question_12():
    print("Question 12 - ")

    return_to_menu()
     

def Question_13():
    print("Question 13 - ")

    return_to_menu()

def Question_14():
    print("Question 14 - ")

    return_to_menu()
    

def Question_15():
    print("Question 15 - ")

    return_to_menu()
    

def Question_16():
    print("Question 16 - ")

    return_to_menu()
       

def Question_17():
    print("Question 17 - ")

    return_to_menu()


def Question_18():
    print("Question 18 - ")

    return_to_menu()


def Question_19():
    print("Question 19 - ")

    return_to_menu()


def Question_20():
    print("Question 20 - ")

    return_to_menu()
    

def Question_21():
    print("Question 21 - ")

    return_to_menu()
 

def Question_22():
    print("Question 22 - ")

    return_to_menu()
      

def Question_23():
    print("Question 23 - ")

    return_to_menu()
       

def Question_24():
    print("Question 24 - ")

    return_to_menu()
    

def Question_25():
    print("Question 25 - ")

    return_to_menu()
   

def Question_26():
    print("Question 26 - ")

    return_to_menu()

main()
