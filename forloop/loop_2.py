#////////////////////////////////
# write a program to find the largest number in a list
# numbers = [3, 6, 2, 11, 10 ]
# max = numbers[0]
# for number in numbers:    
#     if number > max:
#         print(number)
#         max = number
      
# print('Max: ', max)

#/////////////////////////////////
# new_list=[]
# input_n=int(input("Enter the number of elements: "))
# for x in range(input_n):
#     new_list.append(x)  
# print(new_list)


#////////////////////
# my_list=[]
# for i in range(5):
#     my_list.append(int(input()))
# print(my_list)

# #/////////////////////////
# num = int(input("Enter an integer number: "))
# remainder = num % 2
# if remainder == 0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")

#/////////////////////////

# command = ''
# while True:
#     command = input(" > ")
#     if command.lower() == 'stop':
#         break 

#     remainder = int(command) % 2
#     if remainder == 0:
#         print(f"{command} is an even number")
#     else:
#         print(f"{command} is an odd number")


#///////////////////
# list=[5,4,10,8,15,7,9,30,205,55,202,155,199,1000]
# gen_list=[]
# gen_list1=[]
# for i in list:

#     remainder=i % 5
#     if remainder==0:
#         gen_list.append(i)
#     else:
#         gen_list1.append(i)
# print(gen_list)
# print(gen_list1)

#///////////////////
# list_len = int(input("List length > : "))
# odd_list = []
# even_list = []
# total_list = []

# for i in range(list_len):
#     num = int(input("Enter an integer number: "))
#     total_list.append(num)
#     remainder = num % 2
#     if remainder == 0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)
# print(even_list)
# print(odd_list)
# print(total_list)

#////////////////////////////////////
# list=[2,3,5,4,8,7,4,4,4,2,2,5]

# gen_list=[]

# for i in list:
#     if i not in gen_list:
#         gen_list.append(i)
# print(gen_list)


#////////////////////////////////////

# pass_true = 'password'

# ps = ""

# while ps != pass_true:
#     ps = input("Enter parol: ")

# print("Yuo entred this system")


#////////////////////////////////////
# N = 20
# i = 1

# while i <= N:
#     if i % 3 == 0:
#         print(i)
#     i += 1

#////////////////////////////////////
# nums = [3, 9, 5, 11, 15, 11]

# flFind = False
# i = 0

# while i < len(nums):
#     print(f'nums[{i}] - {nums[i]}')
#     flFind = nums[i] % 2 == 0   

#     if flFind:
#         break
#     i += 1

# print(flFind)

#////////////////////////////////////
# s = 0
# d = 1

# while d != 0:
#     d = int(input('Enter integer value: '))
#     if d % 2 == 0:
#         continue
#     s += d
#     print("sum = " + str(s))


# #////////////////////////////////////
# # s = 1/2 + 1/3 +1/4 + ... + 1/1000

# s = 0
# for i in range(2, 1001):
#     s += 1/i
# print(s)

# #////////////////////////////////////
# n = int(input("Enter integer number not more than 100: "))

# if n < 1 or n > 100:
#     print('Not correct number')

# else:
#     p = 1
#     for i in range(1, n +1):
#         p *= i

# print(f'Factorial {n}! = {p}')

# # #////////////////////////////////////
# digs = [4, 3, 100, -53, -30, 1, 34, -8]

# for i in range(len(digs)):
#     if 10 <= abs(digs[i]) <= 99:
#         digs[i] = 0

# print(digs)

# #//////////// enumerate()  ////////////////////////
# digs = [4, 3, 100, -53, -30, 1, 34, -8]

# for i, d in enumerate(digs):
#     print(f'index-{i}, value-{d}')

# #//////////// enumerate()  ////////////////////////

# for i, d in enumerate(digs):
#     if 10 <= abs(d) <= 99:
#         digs[i] = 0

# print(digs)



# a = [i for i in [11, 12, 23, 44, 56, 60, 77]]

# print(a)


#///////////////////////////////////
# N = 6

# # a = [0] * N
# # for i in range(N):
# #     a[i] = i**2   

# # a = []
# # for i in range(N):
# #     a.append(i**2)


# a = [i**2 for i in range(N)]
# print(a)


#///////////////////////////////////
# N = 7
# a = [i % 2 == 0 for i in range(N)]

# print(a)

#///////////////////////////////////
# d_inp = input("Enter intiger number: ")
# # print(d_inp)

# a = [i for i in d_inp.split()]
# print(a)


# #///////////////////////////////////
# a = [i for i in range(-10, 10) if i < 0]
# a = [i for i in range(-10, 10) if i % 2 == 0]
# a = [i for i in range(-10, 10) if i % 2 != 0]
# a = [i for i in range(-10, 10) if i % 2 == 0 and i % 3 == 0]

# print(a)

#///////////////////////////////////
# d= [4, 3, 5, 0, 8, 122, -8, 9, 11, 22]

# a = ['even' if i % 2 == 0 else 'odd' for i in d if i != 0 ]

# print(a)


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






