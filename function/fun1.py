
#/////////////////////////////////////////
# BMI calculator
# we have trhee parameters name, height_m, weight_kg

# name1 ='elyor'
# height_m1 = 1.8
# weight_kg1 = 90

# name2 = "elyor's sister"
# height_m2 = 1.8
# weight_kg2 = 60

# name3 = "elyor's brother"
# height_m3 = 1.9
# weight_kg3 = 85

# def bmi_calculator(name, height_m, weight_kg):
#      bmi = weight_kg / (height_m) ** 2
     
#      print(name + ' is', + bmi)
#      if bmi < 25:
#          return name + ' is not overweight'
#      else:
#          return name + ' is overweight'

# result1 = bmi_calculator(name1, height_m1, weight_kg1)
# result2 = bmi_calculator(name2, height_m2, weight_kg2)
# result3 = bmi_calculator(name3, height_m3, weight_kg3)
# print(result1)
# print(result2)
# print(result3)

# //////////////////////////////////////////////////////
# def add_sub(x,y):
#     c=x+y
#     d=x-y
#     g=x+y
#     return c,d,g
# result1,result2,result3=add_sub(3,8)
# print(result1,result2,result3)


#////////////////////////////
# def greet(name,lname):
#     print(f'Hi {name} {lname}')

# greet('John','Smith')

#////////////////////////////
# context = {}
# def add_person(name,lname, age):   
#     context['name'] = name
#     context['lname'] = lname 
#     context['age'] = age   
   
#     print(context)

# add_person('John','Smith',25)

#////////////////////////////

# context = {}
# def add_person(name, lname, age):   
#     context['name'] = name
#     context['lname'] = lname 
#     context['age'] = age   
#     return context  

# # print(add_person('John','Smith',25))
# add_person('John','Smith',25)

# for i in context.values():
#     print(i)

#////////////////////////////
# name = 'John'
# lname = 'Smith'
# age = 26

# context = {}

# def add_person():   
#     context['name'] = name
#     context['lname'] = lname 
#     context['age'] = age
#     return context 

# add_person()

# for i in context.values():
#     print(i)

# #////////////////////////////
# persons = []

# def add_person(name, lname, age):
    

#     person = {
#             "name": name,
#             "lname": lname,
#             "age": age
#         }   
#     persons.append(person)
#     return persons 

# add_person('Elyor','Dusnazarov', 25)
# add_person('Mohinur','Qodirova', 24)
# add_person('Nilufar','Muminjonova', 8)
# add_person('Ahror','Muminjonov', 24)

# print(persons)

# for i in persons:
#     print(i)


#////////////////////////////
# names = ['Elyor', 'Mohinur', 'Nilufar','Ahror']
# lnames = ['Dusnazarov', 'Qodirova', 'Muminjonova', 'Muminjonov']
# ages = [24, 23, 8, 6]

# persons = []

# def add_person(n):
#     for i in range(n):
#         person = {
#             "name": names[i],
#             "lname": lnames[i],
#             "age": ages[i]
#         }   
#         persons.append(person)

#     return persons 

# add_person(4)

# print(persons)

# for i in persons:
#     print(i)

# # //////////// function ////////////////////////
# import random

# names = ['John', 'Elyor', 'Adam', 'Umid', 'Shuhrat', 'Muhtasar']
# majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


# def people_list(num_people):
#     result = []
#     for i in range(num_people):
#         person = {
#                     'id': i,
#                     'name': random.choice(names),
#                     'major': random.choice(majors)
#                 }
#         result.append(person)
#     return result


# people_list = people_list(4)

# for people in people_list:
#     print(people)


#///////////////////////////////////

# def get_sqrt(x):
#     if x < 0:
#         return None
#     res = x**0.5    
#     return res 


# # def get_sqrt(x):
# #     res = None if x < 0 else x**0.5
# #     return res
    

# a = get_sqrt(16)
# print(a)

#///////////////////////////////////
# def get_sqrt(x):
#     res = None if x < 0 else x**0.5
#     return res, x


# a, b = get_sqrt(16)
# print(a, b)

#///////////////////////////////////
# def get_max(a, b):
#     return a if a > b else b


# x, y = 5, 7
# print(get_max(x, y))

#///////////////////////////////////
# def get_max(a, b):
#     return a if a > b else b


# x, y, z = 5, 7, 10
# print(get_max(y, z))
# print(get_max(x, get_max(y, z)))

#///////////////////////////////////
# def get_max(a, b):
#     return a if a > b else b

# def get_max2(a, b, c):
#     return get_max(a, get_max(b, c))


# x, y, z = 5, 7, 10
# print(get_max2(x, y, z))

#///////////////////////////////////

# PERIMETR = False

# if PERIMETR:
#     def get_rect(a, b):
#         return 2 * (a + b)

# else:
#     def get_rect(a, b):
#         return a * b

# print(get_rect(1.5, 2.8))   

# /////////////////////////////////
# def even(x):
#     # if x == 0:
#     #   return None   
#     # return x % 2 == 0

#     return None if x == 0 else x % 2 == 0

# for i in range(5):   
#    print(even(i))

#////////////////////////////////
# def even(x):
       
#     if x == 0:
#        return None
#     return x % 2 == 0

#     # return None if x == 0 else x % 2 == 0  
   

# for i in range(10):
#     if even(i):
#       print(i)
      

# #///////////////////////////////////
# def get_V(a, b, c):
#     print(f'a = {a}, b = {b}, c = {c}')

#     return a * b *c

# # v = get_V(1, 2, 3)
# v = get_V(b=1, a=2, c=3)
# print(v)


#///////////////////////////////////
# def get_V(a, b, c, verbose=False):
#     if verbose:
#         print(f'a = {a}, b = {b}, c = {c}')

#     return a * b *c

# # v = get_V(1, 2, 3)
# v = get_V(b=1, a=2, c=3)
# print(v)


# #///////////////////////////////////
# def add_value(value, lst=[]):
#     lst.append(value)
#     return lst

# l = add_value(1)
# l = add_value(2)
# print(l)


# #///////////////////////////////////
# def add_value(value, lst=None):
#     if lst is None:
#         print(lst is None)
#         lst = []
#     lst.append(value)
#     return lst

# l = add_value(1)
# l = add_value(2,l)
# print(l)

# #///////////////////////////////////

# def os_path(*args):
#     print(args)

# os_path("F:\\~stepik.org","Dobri, Dobriy Python"," 39\\p39. Funksiy.docx")

#///////////////////////////////////

# def os_path(*args):
#     path = "\\".join(args)
#     return path


# p = os_path("F:\\~stepik.org","Dobri, Dobriy Python"," 39\\p39. Funksiy.docx")
# print(p)



#///////////////////////////////////
def os_path(*args, **kwargs):   
    path = kwargs['sep'].join(args)
    return path


p = os_path("F:\\~stepik.org",
            "Dobri, Dobriy Python",
            " 39\\p39. Funksiy.docx",
            sep='/', trim=True
            )
print(p)












