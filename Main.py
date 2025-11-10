###This is the Bank chat bot
print("Welcome to the bank chatbot!")
name = input("What is your name? ").capitalize()
age = int(input(f"Hello {name}, how old are you? (type this as an integer). "))
print(f"Hello {age}-year-old {name}, how can I help you?")
SetUpAccount = 0
while True:
    print("\nExplore accounts (1)\nSet up account (2)\nExit the program (3)")
    choice = input("Pick an option: ")

    if choice == '1':
        print("At Code2CollegeBank we have 3 different accounts.")
        if age < 18:
            print("Since you are younger than 18, you only have one option for an account.")
            print("The only account you can have is a debit account.")
            print("A debit account is a bank account that lets you spend money you already have directly from your balance.")
            print("If you would like to set one up please press 2")
            SetUpAccount = '1'
        else:
            print("The three account options we have at Code2CollegeBank are debit (1), credit (2), and savings (3).")
            AccountExplore = input('What account would you like to explore? ')
            
            if AccountExplore == '1':
                print("\nA debit account is a bank account that lets you spend money you already have directly from your balance.")
                print("If you would like to set one up please press 2.")
                SetUpAccount = '1'
            elif AccountExplore == '2':
                print("\nA credit account lets you borrow money up to a limit and pay it back later, usually with interest.")
                print("If you would like to set one up please press 2.")
                SetUpAccount = '2'
            elif AccountExplore == '3':
                print("\nA savings account helps you save money safely and can earn you interest over time.")
                print("If you would like to set one up please press 2.")
                SetUpAccount = '3'
            else:
                print("That is not a valid account choice.")

    elif choice == '2':
        print("Hello and I will guide you to set up an account.")
        if SetUpAccount == 0:
            print("You have not chosen an account yet please press 1 to chose an account.")
        elif SetUpAccount == '1':
            print("Hello you have chosen to set up a debit account")
            print("To set up a debit account, you will need to bring your SSN and ID, and a parent if your under 18, to the bank.")
            print("To set up this account please visit your nearest C2C bank and tell them your age and name.")
        elif SetUpAccount == '2':
            print("Hello, you have chosen to set up a credit card")
            print("Here with the chatbot you can discuss your credit card limit")
            CreditScore = int(input("What is your credit score?"))
            if CreditScore > 800:
                print("The limit on your credit card will be 10,000 dollars.")
                limit = 10000
                print(f"To set up your account please visit your nearest C2C bank and they will help you set up your credit card with a limit of {limit}.\nThey will also ask you to verify your age and credit score.")
            elif CreditScore>= 600 and CreditScore <= 800:
                print("The limit on your credit card is 5,000 dollars.")
                limit = 5000
                print(f"To set up your account please visit your nearest C2C bank and they will help you set up your credit card with a limit of {limit}.\nThey will also ask you to verify your age and credit score.")
            elif CreditScore <600 and CreditScore>=450:
                print("The limit on your credit card is 3,000 dollars.")
                limit = 3000
                print(f"To set up your account please visit your nearest C2C bank and they will help you set up your credit card with a limit of {limit}.\nThey will also ask you to verify your age and credit score.")
            else:
                print("The limit on your credit card is 1,500 dollars.")
                limit = 1500
                print(f"To set up your account please visit your nearest C2C bank and they will help you set up your credit card with a limit of {limit}.\nThey will also ask you to verify your age and credit score.")
        elif SetUpAccount == '3':
            print("Hello you have chosen to set up a savings account.")
            
            MoneyInS = int(input("How much money are you going to put in your savings account?"))
            Years = int(input("How many years are you going to leave the money in the account?"))
            InterestRatePick = int(input("There are 2 options of intrest:\nOption 1 5% press 1\nOption 2 3% press 2\nIf you don't pick one of these you will be automatically assigned 3%."))
            if InterestRatePick == 1:
                IntrestYear = round(((1.05**Years)* MoneyInS) - MoneyInS)
                print(F'You will have made {IntrestYear} in {Years} years.')
            else:
                IntrestYear = ((1.03**Years)* MoneyInS) - MoneyInS
                print(F'You will have made {IntrestYear} in {Years} years.')
            print("To set up your savings account please visit your nearest C2C bank and verify your information.")
            
            
           
            
                

    

    elif choice == '3':
        print(f"Goodbye {name}, see you later!")
        break  

    else:
        print("That is not a valid choice. Please pick from 1, 2, or 3.")
