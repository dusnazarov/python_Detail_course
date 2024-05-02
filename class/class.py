#////////////////////////////////////////////
# class MyClass:
  
#   def printer(self):    
#     return self
 
# print(MyClass)

# p1 = MyClass()
# print(p1)
# print(p1.printer())

# p2 = MyClass()
# print(p2)
# print(p2.printer())

# p3 = MyClass()
# print(p3)
# print(p3.printer())

# # # #////////////////////////////////////////////
# class MyClass:
#     x = 3
#     y = 4
    
#     def add_nums():
#         print(MyClass.x + MyClass.y)    

# """
#     x, y lar Myclass ni atributlari.
#     Agar o'zgartirsak MyClass.x va MyClass.y larga
#     yangi qiymat beramiz.

# """
# # MyClass.x = 5 
# # MyClass.y = 6 
  
# print(MyClass.x)
# print(MyClass.y)
# print(MyClass.add_nums())
# print(MyClass.__dict__) 

# #////////////////////////////////////////////
# class MyClass:
#     x = 3
#     y = 4     
 
   
#     def add_nums(x, y):
#         print(x + y)
# """
#     x, y lar Myclass ni atributlari.    

# """
           

# print(MyClass.x)
# print(MyClass.y)
# print(MyClass.add_nums(MyClass.x, MyClass.y))
# print(MyClass.__dict__)


# #////////////////////////////////////////////
# class MyClass:

   
#     def add_nums(x, y):
#         print(x + y)    
       
# """
#     x, y lar Myclass ni atributlari EMAS.
#     shunchaki MyClass ichiga yozilgan funksiy
    

# """
# print(MyClass.add_nums(3, 4))
# print(MyClass.__dict__)



# #////////////////////////////////////////////
# class MyClass:
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

   
#     def add_nums(self, z):
#         print(self.x + self.y + z)    
       

# p = MyClass(3, 4)
# print(p.add_nums(3))
# print(p.__dict__)
# print(MyClass.__dict__)



#////////////////////////////////////////////
class Point:
   
    def class_print():
        print('call the method set_corords')


    def func_print(self):
        print(f'call method set_corords >> {self}')

    


# print(Point.class_print)
# print(Point.class_print())

pt = Point()
print(pt.func_print)
print(pt.func_print())

# pt = Point()
# print(Point.func_print(pt))









