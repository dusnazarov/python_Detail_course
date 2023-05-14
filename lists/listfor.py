#/////////////////////
# thislist=["apple","orange","cherry", "banana"]
# for x in thislist:
#     print(x)

#///////////////////////////
# short forms
# fruits=["apple","orange","cherry", "banana","kiwi","mango"]
# newlist=[x.upper() for x in fruits]
# print(newlist)

#///////////////////////////
# full forms
# fruits=["apple","orange","cherry", "banana","kiwi","mango"]
# new_list=[]
# for x in fruits:
#     new_list.append(x.upper())
# print(new_list)

#///////////////////////////
# short forms
# fruits=["apple","orange","cherry", "banana","kiwi","mango"]
# new_list=[x for x in fruits if "a" in x]
# print(new_list)

#///////////////////////////
# full forms
# fruits=["apple","orange","cherry", "banana","kiwi","mango"]
# new_list=[]
# for x in fruits:
#     if "a" in x:
#         new_list.append(x)
# print(new_list)

#///////////////////////////
# short forms
# fruits=["apple","orange","cherry", "banana","kiwi","mango"]
# new_list=[f"hello {x}" for x in fruits]
# print(new_list)

#///////////////////////////
# full forms
# fruits=["apple","orange","cherry", "banana","kiwi","mango"]
# new_list=[]
# for x in fruits:
#     new_list.append(f"hello {x}")
# print(new_list)

#/////////////////////////////////
# new_list=[]
# input_n=int(input("Enter the number of elements: "))
# for x in range(input_n):
#     new_list.append(x)
#     print(x)
# print(new_list)

#///////////////////////////////////
# len_list=int(input("Enter the length of list: "))
# gen_list=[]
#
# for x in range(len_list):
#     list_element=int(input("Enter the elements of the list: "))
#     gen_list.append(list_element)
#     print(gen_list)
#     print(x)
# if gen_list[0]==gen_list[-1]:
#     print("True")
# else:
#     print("False")
#
# print(gen_list)

#/////////////////////////////
# len_list=int(input("Enter the length of list: "))
# gen_list=[]
#
# for x in range(len_list):
#     list_element=int(input("Enter the elements of the list: "))
#     gen_list.append(list_element)
#
# print(gen_list)


#////////////////////
# my_list=[]
# for i in range(5):
#     my_list.append(int(input()))
# print(my_list)

#/////////////////////////
# number=int(input("Enter an integer number: "))
# remainder=number % 2
# if remainder==0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")


#///////////////////
# list=[5,4,10,8,15,7,9,30,205,55,202,155,199,1000]
# gen_list=[]
# gen_list1=[]
# for i in list:
#
#     remainder=i % 5
#     if remainder==0:
#         gen_list.append(i)
#     else:
#         gen_list1.append(i)
# print(gen_list)
# print(gen_list1)

#///////////////////
# list_len=int(input("Enter an integer number: "))
# gen_list=[]
# for i in range(list_len):
#     number=int(input("Enter an integer number: "))
#     remainder=number % 5
#     if remainder==0:
#         gen_list.append(number)
# print(gen_list)

#////////////////////////////////////
# list=[2,3,5,4,8,7,4,4,4,2,2,5]
#
# gen_list=[]
# for i in list:
#     if i not in gen_list:
#         gen_list.append(i)
# print(gen_list)


