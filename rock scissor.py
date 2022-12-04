import random

Your_point = 0
Cpu_point = 0
while True:

    print('''Enter:
    r for rock
    p for paper
    s for sciesar''')

    lst = ['rock', 'paper', 'sciesar']

    n = 1

    print()
    user_input = input("ENTER YOU CHOICE:-")
    print()
    choice = random.choice(lst)
    print("computer choice:-",choice)
    if user_input == 'r':
        if choice == 'sciesar':
            Your_point += 1
            print("Winner!")
        elif choice == 'paper':
            Cpu_point += 1
            print("Losser")

    if user_input == 'p':
        if choice == 'rock':
            Your_point += 1
            print("Winner!")
        elif choice == 'sciesar':
            Cpu_point += 1
            print("Losser")

    if user_input == 's':
        if choice == 'paper':
            Your_point += 1
            print("Winner!")
        elif choice == 'rock':
            Cpu_point += 1
            print("Losser")
    if user_input=="s":
        if choice=="sciesar":
            print("tie")
    if user_input == "p":
        if choice == "papper":
            print("tie")
    if user_input == "r":
        if choice == "rock":
            print("tie")
    print()
    print()

    print(f"Your points {Your_point}")
    print(f"CPU's points {Cpu_point}")

    print()
    v= input("enter yes to end the program yes/no:--")


    if v==("yes"):
        print("your points:-",Your_point)
        print("CPU's points:-",Cpu_point)
        print("""
        THANKS FOR PLAY A GAME 
        """)
        break
    else:
        continue
