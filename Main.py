print("Welcome to the food ordering chatbot!")
name = input("what is your name")
age = int(input("Hello " +  name + ", how old are you?"))
print(f"Hello {age} year old {name}, how can I help you?")
print(" 1.Place holder1\n 2.Place holder2\n 3.Place holder3\n 4.Exit the program")
choice = input("Pick an option")
if choice == '1':
    print("Placeholder 1")
elif choice == '2':
    print("Placeholder 2")
elif choice == '3':
    print("Placeholder 3")
elif choice == '4':
    print(f"Goodbye {name} see you later")
else:
    choice = input("That is not a valid choice try again. Pick from 1,2,3,or 4")