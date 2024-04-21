

#///////////////////////////////////////
# listA = ['a','e','i','o','u']

# iter_listA = listA.__iter__()

# print(iter_listA.__next__())
# print(iter_listA.__next__())
# print(iter_listA.__next__())
# print(iter_listA.__next__())
# print(iter_listA.__next__())

#///////////////////////////////////////
# listA = ['a','e','i','o','u']

# iter_listA = iter(listA)

# print(next(iter_listA))
# print(next(iter_listA))
# print(next(iter_listA))
# print(next(iter_listA))
# print(next(iter_listA))

#///////////////////////////////////////
# listA = ['a','e','i','o','u']

# iter_listA = iter(listA)

# for i in iter_listA:
#     print(i)

# #//////////////////////////////////////////////

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1   
#     return self

#   def __next__(self):   
#     x = self.a  
#     self.a += 1
#     return x

# myclass = MyNumbers()

# myiter = iter(myclass)

# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))

# for i in myiter:
#   print(i)

#//////////////////////////////////////////////
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)

# //////////////////////////////////
class MyListOf4:

    def __init__(self, n1, n2, n3, n4):
        self.a = n1
        self.b = n2
        self.c = n3
        self.d = n4

        self.max = 4

    def __iter__(self):
        self.start = 0
        return self
    
    def __next__(self):        
        self.start +=  1
      
        if (self.start > self.max):
            raise StopIteration
        if (self.start == 1):
            return self.a
        if (self.start == 2):
            return self.b
        if (self.start == 3):
            return self.c
        if (self.start == 4):
            return self.d

l1 = MyListOf4(12, 5, 7, 8)

for i in l1:
    print(i)
















