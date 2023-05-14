




#/////////////////////////////////////////////
# Guess Game
# secret_number=9
# guess_count=0
# guess_limit=3

# while guess_count<guess_limit:
#     guess = int(input('Guess: '))
#     guess_count+=1
#     if guess==secret_number:
#         print('You won!')
#         # break

# else:
#     print('Sorry you failed !')    

#///////////////////////////////////
# i=0
# while i<5:
#     input('Enter numers :')
#     i+=1

#///////////////////////////////////
# i=0
# while i<5:
#     num=input('Enter numers :')
#     print(num)
#     i+=1

#///////////////////////////////////
# i=0
# while i<3:
#     num=int(input('Enter numers :'))
#     i+=1   
#     if num==2:
#         print('You won')        
#         break

# else:
#     print('Sorry, you failed!')


# 1) ////////////////////////////////////////
# command=""
# while command.lower() !="quit":
#     command=input("> ")
#     if command.lower()=="start":
#         print("Car started ...")
#     elif command.lower()=="stop":
#         print("Car stopped.")

#     elif command=="help":
#         print("""
#         start - to start the car
#         stop - to stop the car 
#         quit - to quit
        
#         """)
#     else:
#         print("Sorry, I don't understand that")


# 2) ////////////////////////////////////////
# command=""
# while command !="quit":
#     command=input("> ").lower()
#     if command=="start":
#         print("Car started ...")
#     elif command=="stop":
#         print("Car stopped.")

#     elif command=="help":
#         print("""
#         start - to start the car
#         stop - to stop the car 
#         quit - to quit
        
#         """)
#     else:
#         print('Sorry, i do not understand that!')

# 3) ////////////////////////////////////////
# the quit comandasini yozganda while to'htayabdida else qismi ishlab ketyabdi.
# command=""
# while command !="quit":
#     command=input("> ").lower()
#     if command=="start":
#         print("Car started ...")
#     elif command=="stop":
#         print("Car stopped.")

#     elif command=="help":
#         print("""
#         start - to start the car
#         stop - to stop the car 
#         quit - to quit
        
#         """)
#     else:
#         print('Sorry, i do not understand that!')

# 3) ////////////////////////////////////////
# muamo hal bo'ldi lekin, command=="quit" ikki marta takrorlanib qolyabdi shuning uchun.
# command=""
# while command !="quit":
#     command=input("> ").lower()
#     if command=="start":
#         print("Car started ...")
#     elif command=="stop":
#         print("Car stopped.")

#     elif command=="help":
#         print("""
#         start - to start the car
#         stop - to stop the car 
#         quit - to quit
        
#         """)
#     elif command=="quit":
#         break

#     else:
#         print('Sorry, i do not understand that!')

# 3) ////////////////////////////////////////
# muamo hal bo'ldi lekin, command=="quit" ikki marta takrorlanib qolyabdi shuning uchun.
# Whilw True: break bo'lmagincha davom etaveradi.
# command=""
# while True:
#     command=input("> ").lower()
#     if command=="start":
#         print("Car started ...")
#     elif command=="stop":
#         print("Car stopped.")

#     elif command=="help":
#         print("""
#         start - to start the car
#         stop - to stop the car 
#         quit - to quit
        
#         """)
#     elif command=="quit":
#         break

#     else:
#         print('Sorry, i do not understand that!')

# 4) ////////////////////////////////////////
# bu to'liq qism
command=""
started=False
while True:
    command=input("> ").lower()
    if command=="start":
        if started:
            print("Car is already started !")
        else:
            started=True
            print("Car started ...")
    elif command=="stop":
        if not started:
            print("Car is already stopped !")
        else:
            started=False
            print("Car stopped.")

    elif command=="help":
        print("""
        start - to start the car
        stop - to stop the car 
        quit - to quit
        
        """)
    elif command=="quit":
        break

    else:
        print('Sorry, i do not understand that!')


