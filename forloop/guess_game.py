
#///////////////  Guess Game  //////////////////////////////
# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You got it in', guess_count, 'guesses')
#         break

# else:
#     print('Sorry you failed !')    




# ////////////////////////////////////////

# command=""
# while command != "quit":
#     command = input("> ").lower()
#     if command == "start":
#         print("Car started ...")
#     elif command == "stop":
#         print("Car stopped.")

#     elif command == "help":
#         print("""
#         start - to start the car
#         stop - to stop the car 
#         quit - to quit
        
#         """)
#     elif command == "quit":
#         break

#     else:
#         print('Sorry, i do not understand that!')

#////////////////////////////////////////

# command=""
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         print("Car started ...")
#     elif command == "stop":
#         print("Car stopped.")

#     elif command == "help":
#         print("""
#         start - to start the car
#         stop - to stop the car 
#         quit - to quit
        
#         """)
#     elif command == "quit":
#         break

#     else:
#         print('Sorry, i do not understand that!')

# ////////////////////////////////////////
command=""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started !")
        else:
            started = True
            print("Car started ...")
    elif command == "stop":
        if not started:
            print("Car is already stopped !")
        else:
            started = False
            print("Car stopped.")

    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car 
        quit - to quit
        
        """)
    elif command == "quit":
        break

    else:
        print('Sorry, i do not understand that!')


