import random

# To-Do List - stores tasks in a list that changes while program runs
tasks = []

# Tool 1: To-Do List
def todo_list():
    print("\n--- To-Do List ---")
    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Back to main menu")
        choice = input("Choose (1-4): ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print(f"Added: {task}")
        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks yet!")
            else:
                print("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == "3":
            if len(tasks) == 0:
                print("No tasks to remove!")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                num = input("Enter task number to remove: ")
                if num.isdigit():
                    num = int(num)
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid task number!")
                else:
                    print("Please enter a number!")
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please choose 1-4.")

# Tool 2: Simple Calculator
def calculator():
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Operations: +  -  *  /")
        op = input("Enter operation: ")

        if op == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif op == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif op == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif op == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation! Use + - * /")
    except ValueError:
        print("Please enter valid numbers!")

# Tool 3: Number Guessing Game
def guessing_game():
    print("\n--- Number Guessing Game ---")
    print("I am thinking of a number between 1 and 20!")
    secret = random.randint(1, 20)
    attempts = 0
    while True:
        guess = input("Guess the number: ")
        if not guess.isdigit():
            print("Please enter a number!")
            continue
        guess = int(guess)
        attempts += 1
        if guess < secret:
            print(f"{guess} is too low! Try again.")
        elif guess > secret:
            print(f"{guess} is too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts!")
            break

# Tool 4: Name Formatter
def name_formatter():
    print("\n--- Name Formatter ---")
    name = input("Enter your full name: ").strip()
    if name == "":
        print("You did not enter a name!")
    else:
        print(f"Original: {name}")
        print(f"Uppercase: {name.upper()}")
        print(f"Lowercase: {name.lower()}")
        print(f"Title Case: {name.title()}")
        print(f"Hello, {name.title()}! Welcome to the toolkit!")

# Main menu loop
print("Welcome to My Personal Mini-Toolkit!")

while True:
    print("\n--- MAIN MENU ---")
    print("1. To-Do List")
    print("2. Simple Calculator")
    print("3. Number Guessing Game")
    print("4. Name Formatter")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        todo_list()
    elif choice == "2":
        calculator()
    elif choice == "3":
        guessing_game()
    elif choice == "4":
        name_formatter()
    elif choice == "5":
        print("Thank you for using My Toolkit! Goodbye!")
        break
    else:
        print("Invalid choice! Please choose 1-5.")
