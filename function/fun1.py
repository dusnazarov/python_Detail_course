
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















