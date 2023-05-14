
# 1), 2), 3), 4), ////////////////////////////////////////////////
"""
    if it's hot
        It's a hot day
        Drink plenty of water
    otherwise if it's cold
        It's a cold day
        Wear warm clothes
    otherwise
        It's a lovely day

"""


# 1) /////////////////////////////////////
# is_hot=True

# if is_hot:
#     print("It's  a hot day")

# print("Enjoy your day")   

# 2) /////////////////////////////////////
# is_hot=False

# if is_hot:
#     print("It's  a hot day")
    
# print("Enjoy your day")   

# 3) /////////////////////////////////////
# is_hot=False

# if is_hot:
#     print("It's  a hot day")
#     print("Drink plenty of water")
# else:
#     print("It's a cold day")
#     print("Wear warm clothes")
    
# print("Enjoy your day")   

# 4) /////////////////////////////////////
# is_hot=False
# is_cold=True

# if is_hot:
#     print("It's  a hot day")
#     print("Drink plenty of water")

# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
    
# else:    
#     print(" It's a lovely day")   

# print("Enjoy your day") 


# 5) ///////////////////////////////////////////
"""
    Price of a house is $1M.
    if buyer has good creadit,
        they need to put down 10%
    otherwise
        They need to put down 20%
    Print the down payment

"""

# price=1000000
# has_good_creadit=True

# if has_good_creadit:
#     down_payment= 0.1 * price

# else:
#     down_payment= 0.2 * price

# print(f"Down payment : ${down_payment}")

# 6) ///////////// logical AND  ///////////////////////////////////////////
"""
    If applicant has high income AND good creadit 
        Eligible for loan
"""

# has_high_income = True
# has_good_credit = True

# if has_high_income and has_good_credit:
#     print(" Eligible for loan")

# 7) ///////////// logical AND  ///////////////////////////////////////////
"""
    If applicant has high income AND good creadit 
        Eligible for loan
"""

# has_high_income = False
# has_good_credit = True

# if has_high_income and has_good_credit:
#     print(" Eligible for loan")


# 8) ///////////// logical OR ///////////////////////////////////////////
"""
    If applicant has high income OR good creadit 
        Eligible for loan
"""

# has_high_income = False
# has_good_credit = True

# if has_high_income or has_good_credit:
#     print(" Eligible for loan")

# 9) ///////////// logical OR ///////////////////////////////////////////
"""
    If applicant has high income OR good creadit 
        Eligible for loan
"""

# has_high_income = False
# has_good_credit = False

# if has_high_income or has_good_credit:
#     print(" Eligible for loan")

#  10)  /////////////// AND NOT ////////////////////////

"""
    If applicant has good cedit AND dosn't have a creminal record 
        Eligible for loan
"""

# has_good_creadit= True
# has_criminal_record=False

# if has_good_creadit and not has_criminal_record:
#     print(" Eligible for loan ")


# 11) //// Comparision ////////////////
"""
    if temperature is greater than 30
        it's a hot day
    otherwise if it's less than 10
        it's a cold day
    otherwise
    it's neither hot nor cold

"""

# temperature= 30

# if temperature > 30:
#     print(" It' a hot day")

# else:
#     print(" It' not a hot day")


# 12) ////////////////////////////////////////////

""" 
    if name is less than 3 characters long
        name must be at least 3 characters
    otherwise if it's more than 50 characters long
        name must be a maxsimum of 50 characters
    otherwise
    name looks good!

"""

name="Jdddddd"

if len(name) < 3:
    print("name must be at least 3 characters")

elif len(name):
    print("name must be a maxsimum of 50 characters")

else:
    print(" Name looks good!")


# ////////////////////////////////////////////////////
# 3) bu yerda a>b True holat va a<b ham True 

# a=int(input('Enter a : '))
# b=int(input('Enter b : '))

# if a>b:
#     print('the condition of a>b is True')
# elif a<b:
#     print(' the condition of a<b is True')
# elif a==b:
#     print('the condition of a=b is True')
# else:
#     print('try again')


#////////////////////////////////////
# 4) if operatorni logical ko'rinishi.
# "AND"  operatorini ishlatganda ikkala holat ham  True bo'lishi kerak, aks holda else ga o'tib ketadi.
#  AND: both conditions should be true.

# button_1=True
# button_2=True

# if button_1 and button_2:

#     print('logical 4')

# else:
#     print('try again')

# //////////////////////////////
# 4') 4 ni boshqacha usilda ishlangani

# a=int(input('Enter a : '))
# b=int(input('Enter b : '))
# c=int(input('Enter c : '))

# if a>b and b>c:

#     print(f'{a>b} and {b>c}')

# else:
#     print('try again') 


# /////////////////////////////////////////
# 5)  if operatorni logical ko'rinishi.
# bu yerda "OR" operatori islashi uchun,eng kamida ikkidan biri folse yokiy true bo'lsa ishlaydi.
# OR: at least one condition should be true.

# button_1 = True
# button_2 =False

# if button_1 or button_2:

#     print('logical 5')

# else:
#     print('try again')

#/////////////////////////////////
# 5') 5 ni boshqacha usilda ishlanishi.

# a=int(input('Enter a : '))
# b=int(input('Enter b : '))
# c=int(input('Enter c : '))

# if a>b or b>c:

#     print(f'{a>b} and {b>c}')

# else:
#     print('try again')


#/////////////////////////////////
# 6) 
# NOT : bu "AND" va "OR" logical operatorlarni to'gri ishlashini inkor qiladi
# natijada if dan keyingi qatorlar ishlamaydi.

# button_1 =True
# button_2 =False

# if button_1 and not button_2:

#     print('logical 6')

# else:
#     print('try again')

# ///////////////////////////////
# 6') 
# a=int(input('Enter a : '))
# b=int(input('Enter b : '))
# c=int(input('Enter c : '))


# if a>b and not b>c:

#     print(f'{a>b} and {b>c}')

# else:
#     print('try again')


# button_1 = False
# button_2 =False

# if button_1 or not button_2:

#     print('logical 5')

# else:
#     print('try again')



# seceret_num=8
# guess_count=0
# guess_limt=3

# while guess_count<guess_limt:
#     guess_count += 1
#     guess = int(input('Guest :'))
  
#     if guess==seceret_num:
#         print('you won !')
#         break
# else:
#     print('sorry, you failed')

# x=""
# while x!="hello":
#     if x=='bir':
#         print('bir')
#     elif x==('ikki'):
#         print('ikki')
#     else:
#         print('besh')

