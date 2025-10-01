print("Welcome to the bank chatbot!")
name = input("What is your name? ")
age = int(input("Hello " + name + ", how old are you? "))
print(f"Hello {age}-year-old {name}, how can I help you?")

while True:
    print("\nExplore accounts (1)\nSet up account (2)\nExit the program (4)")
    choice = input("Pick an option: ")

    if choice == '1':
        print("At Code2CollegeBank we have 3 different accounts.")
        if age < 18:
            print("Since you are younger than 18, you only have one option for an account.")
            print("The only account you can have is a debit account.")
            print("A debit account is a bank account that lets you spend money you already have directly from your balance.")
        else:
            print("The three account options we have at Code2CollegeBank are debit (1), credit (2), and savings (3).")
            AccountExplore = input('What account would you like to explore? ')
            
            if AccountExplore == '1':
                print("\nA debit account is a bank account that lets you spend money you already have directly from your balance.")
            elif AccountExplore == '2':
                print("\nA credit account lets you borrow money up to a limit and pay it back later, usually with interest.")
            elif AccountExplore == '3':
                print("\nA savings account helps you save money safely and can earn you interest over time.")
            else:
                print("That is not a valid account choice.")

    elif choice == '2':
        print("Placeholder for setting up an account.")

    elif choice == '4':
        print(f"Goodbye {name}, see you later!")
        break  # exits the while loop/program

    else:
        print("That is not a valid choice. Please pick from 1, 2, or 4.")
