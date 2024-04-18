# # ////////////////////////////////////

# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1

# nums = my_range(1, 10)

# print(next(nums))
# print(next(nums))
# print(next(nums))


# # ////////////////////////////////////

# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1

# nums = my_range(1, 10)

# for num in nums:
#     print(num)

# //////////////Generate //////////////////////

# def sentence(sentence):
#     for word in sentence.split():
#         yield word

# my_sentence = sentence('This is a test')

# for word in my_sentence:
#     print(word)


# //////////////Generate //////////////////////

# def gen(n):
#     for i in range(n):
#         yield i

# for i in gen(5):
#     print(i)

# # ////////////// Function //////////////////////

# def square_numbers(nums):
#     result = []

#     for i in nums:
#         result.append(i*i)
#     return result
# list = [1,2,3,4,5]
# my_nums = square_numbers(list)
# print(my_nums)


# # ////////////// Generate //////////////////////
# def square_numbers(nums): 
#     for i in nums:
#         yield (i*i)        
    
# list = [1,2,3,4,5]
# my_nums = square_numbers(list)

# new_list = []
# for n in my_nums:
#     new_list.append(n)

# print(new_list)


# # //////////// function and generate ////////////////////////
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

# def people_generator(num_people):
#     for i in range(num_people):
#         person = {
#                     'id': i,
#                     'name': random.choice(names),
#                     'major': random.choice(majors)
#                 }
#         yield person

# # people_list = people_list(4)

# # for people in people_list:
# #     print(people)

# people_generator = people_generator(4)
# for people in people_generator:
#     print(people)

# ////////////////////////

# def f():
#     return 1
#     return 2
#     return 3
#     return 4
# print(f())

# # ////////////////////////

# def g():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# print(g())

# for x in g():
#     print(x)

# # ////////////////////////
# import string

# def letters():
#     for c in string.ascii_lowercase:
#         yield c

# for letter in letters():
#     print(letter)



# import string library function 
import string 
   
# Storing the value in variable result 
result = string.ascii_lowercase
   
# Printing the value 
print(result) 






    