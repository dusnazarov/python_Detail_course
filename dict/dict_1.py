#//////////////////////////////
# dict = dict(one=1, two=2, three='3', four='4')
# print(dict)

#////////////////////////////////////
# Dict = {}
# my_list = [(1, 'Geeks'), (2, 'For')]
# print(my_list)
 
# # Creating a Dictionary
# # with each item as a Pair
# print("\nDictionary with the use of dict(): ")
# Dict = dict(my_list)
# print(Dict)



#//////////////////////////////
# dict = {}
# dict['fname'] = "Elyor"
# dict['lname'] = "Dusnazarov"
# dict['age'] = 25

# print(dict)

#//////////////////////////////
# key_lst = ["fname", "lname", "age"]

# dict1 = dict.fromkeys(key_lst)
# print(dict1)

# dict2 = dict.fromkeys(key_lst, "defaul person")
# print(dict2)

#////////////////////////////////
# dict = {'fname':"elyor", "lname":"dusnazarov", "age":25}

# # dict_keys = dict.keys()
# # print(dict_keys)


# # dict_values = dict.values()
# # print(dict_values)

# # dict_values = dict.items()
# # print(dict_values)


# # for x in dict:
# #     print(x)

# # for x in dict:
# #     print(dict[x])

# # for x in dict.keys():
# #     print(x)

# # for x in dict.values():
# #     print(x)

# for x, y in dict.items():
#     print(x, y)

# dict.update(
#     {
#     'fname':'elyorjon',
#     'lname': 'Qodirov',
#     'age':35

#     }
# )
# print(dict)

# # the pop() method removes the item with the specified key name 
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

# # The popitem() method removes the last inserted item 
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # thisdict['new'] = 'exist'
# thisdict.popitem()
# print(thisdict)

# # The del keyword removes the item with the specified key name:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)

# # The del keyword can also delete the dictionary completely:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict)

# # The clear() method empties the dictionary:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(thisdict[x])



# ////////////////////////////////////////////////////////
# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# people[3] = {}

# people[3]['name'] = 'Luna'
# people[3]['age'] = '24'
# people[3]['sex'] = 'Female'
# people[3]['married'] = 'No'

# print(people[3])
# print(people)

#////////////////////////////////////
# people = {'person1': {'name': 'John', 'age': '27', 'sex': 'Male'},
#           'person2': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# people['person3'] = {}

# people['person3']['name'] = 'Luna'
# people['person3']['age'] = '24'
# people['person3']['sex'] = 'Female'
# people['person3']['married'] = 'No'

# print(people['person3'])
# print(people)


# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

# for p_id, p_info in people.items():
#     print("\nPerson ID:", p_id)
    
#     for key in p_info:
#         print(key + ':', p_info[key])
# test

#//////////////////////////////////
# people = {'person1': {'name': 'John', 'age': '27', 'sex': 'Male'},
#           'person2': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}



# # dict = people.get('person1', 0) 
# dict = people.get('person3', 0)    
# print(dict)
 

# #////////////////////////////////////
# people = {'person1': {'name': 'John', 'age': '27', 'sex': 'Male'},
#           'person2': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}


# if 'person3' in people:
#     print('Yes')
#     people['person3'] = ['elyor']
    
# else:
#     people['person3'] = [1, 2, 3]

# print(people)

#////////////////////////////////////
# people = {'person1': {'name': 'John', 'age': '27', 'sex': 'Male'},
#           'person2': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}


# if 'person3' in people:
#     print('Yes')   
#     people['person2'].popitem()
#     print(type(people))
    
    
# else:
#     people['person3'] = [1, 2, 3]
#     print(type(people))
# print(people)


# #//////////////////////////////////
# people = {'person1': {'name': 'John', 'age': '27', 'sex': 'Male'},
#           'person2': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}



# # dict = people.get('person1', 0) 
# dict = people.get('person3', 0)    
# print(dict)
 
















