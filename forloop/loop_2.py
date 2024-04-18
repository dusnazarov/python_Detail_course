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
list=[2,3,5,4,8,7,4,4,4,2,2,5]

gen_list=[]

for i in list:
    if i not in gen_list:
        gen_list.append(i)
print(gen_list)
