# /////////////////  raqamlar yig'indisi topish /////////////////////////////////

# num = int(input('Enter a positive integer number : '))

# result = 0
# while num > 0:
#     remainder = num % 10   
#     result = result + remainder    
#     num = num // 10
  
# print('sum is :', result)


# //////////////////////////////////////////////////
# prices = [25, 30, 23, 40, 18]


# # total = 0
# # for price in prices:
# #     total += price

# # i = 0
# # total = 0
# # for i in range(len(prices)):
# #     total += prices[i]


# # total = 0
# # i = 0
# # while i < len(prices): 
# #     total += prices[i]
# #     i += 1


# total = 0
# i = 0
# while True:
#     if i == len(prices):
#         break 
#     total += prices[i]
#     i += 1


# print(f"Total : {total}")

#////////////////  break  /////////////////////////////
# fruits = ["apple", "banana", "cherry","orange"]
# new_list = []

# # for x in fruits:
# #   if x == "cherry":   
# #     break
# #   new_list.append(x)


# # i = 0
# # for i in range(len(fruits)):    
# #     if fruits[i] == "cherry":
# #         break
# #     new_list.append(fruits[i])

# # i = 0
# # while i < len(fruits):    
# #     if fruits[i] == "cherry":
# #         break
# #     new_list.append(fruits[i])
# #     i += 1


# i = 0
# while True:
#     if i > len(fruits):
#         break    
#     if fruits[i] == "cherry":
#         break
#     new_list.append(fruits[i])
#     i += 1

# print(new_list)     

  

#///////////////   continue  /////////////////////////////////////
# fruits = ["apple", "banana", "cherry","orange"]
# new_list = []

# # for x in fruits:
# #   if x == "cherry":   
# #     continue
# #   new_list.append(x)


# # i = 0
# # for i in range(len(fruits)):    
# #     if fruits[i] == "cherry":
# #         continue
# #     new_list.append(fruits[i])

# # i = 0
# # while i < len(fruits):    
# #     if fruits[i] == "cherry":
# #         continue
# #     new_list.append(fruits[i])
# #     i += 1


# i = 0
# while True:
#     if i > len(fruits):
#         break    
#     if fruits[i] == "cherry":
#         continue
#     new_list.append(fruits[i])
#     i += 1

# print(new_list) 

# # /////////  List Comprehension ////////////////////

# squares2 = [x**2 % 5 for x in range(1, 10)]

# print(squares2)


# ////////////////////////////////////////////
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = []

# # new_list = [x for x in fruits if "a" in x]

# # for x in fruits:
# #   if "a" in x:
# #     new_list.append(x)


# # for i in range(len(fruits)):
# #   if "a" in fruits[i]:
# #     new_list.append(fruits[i])

# # i = 0
# # while i < len(fruits):
# #     if "a" in fruits[i]:
# #         new_list.append(fruits[i])
# #     i += 1

# i = 0
# while True:
#     if i == len(fruits):
#         break
    
#     if "a" in fruits[i]:
#         new_list.append(fruits[i])
#     i += 1


# print(new_list)

# # ////////////////////////////////////////////
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# new_list = []

# # new_list = [x for x in fruits if x != "apple"]


# # for x in fruits:
# #     if x != "apple":
# #         new_list.append(x)


# # for i in range(len(fruits)):
# #     if fruits[i] != "apple":
# #         new_list.append(fruits[i])

# # i = 0
# # while i < len(fruits):
# #     if fruits[i] != "apple":
# #         new_list.append(fruits[i])

# #     i += 1

# i = 0
# while True:
#     if i == len(fruits):
#         break

#     if fruits[i] != "apple":
#         new_list.append(fruits[i])
#     i += 1        

# print(new_list)


# # ////////////////////////////////////////////
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = []

# # new_list = [x.upper() for x in fruits]


# # for x in fruits:
# #     new_list.append(x.upper())  


# # for i in range(len(fruits)):
# #     new_list.append(fruits[i].upper())


# # i = 0
# # while i < len(fruits):
# #     new_list.append(fruits[i].upper())
# #     i += 1

# # i = 0
# # while True:
# #     if i == len(fruits):
# #         break
# #     new_list.append(fruits[i].upper())
# #     i += 1

# print(new_list)


#///////////////////////////////////////////////////////
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = []

# # new_list = [x if x != "banana" else "orange" for x in fruits]

# # for x in fruits:
# #     if x != "banana":
# #         new_list.append(x)
# #     else:
# #         new_list.append("orange")

# # for i in range(len(fruits)):
# #     if fruits[i] != "banana":
# #         new_list.append(fruits[i])
# #     else:
# #         new_list.append("orange")

# # i = 0
# # while i < len(fruits):
# #     if fruits[i] != "banana":
# #         new_list.append(fruits[i])
# #     else:
# #         new_list.append("orange")
# #     i += 1
        
# # print(new_list)

# i = 0
# while True:
#     if i == len(fruits):
#         break
#     if fruits[i] != "banana":
#         new_list.append(fruits[i])
#     else:
#         new_list.append("orange")
#     i += 1
        
# print(new_list)

