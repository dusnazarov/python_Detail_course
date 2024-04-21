import sys

# //////////////////////////////////////

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(sys.getsizeof(x))
# print(sys.getsizeof(range(1, 10)))

# for i in x:
#     print(i)

# for i in range(1, 10):
#     print(i)



# # //////////////////////////////////////

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# y = map(lambda i: i**2, x)

# for i in y:
#     print(i)


# # //////////////////////////////////////

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# y = map(lambda i: i**2, x)

# # print(sys.getsizeof(y))
# # print(sys.getsizeof(list(y)))

# # //////////////////////////////////////

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# y = map(lambda i: i**2, x)

# while True:
#     try:
#         value = next(y)
#         print(value)
#     except StopIteration:
#         print('Done')
#         break

# # # //////////////////////////////////////
# class Iter:

#     def __init__(self, n):
#         self.n = n
      

#     def __iter__(self):
#         self.current = -1        
#         return self
    
#     def __next__(self):
#         self.current += 1

#         if self.current >= self.n:
#             raise StopIteration
#         return self.current

# x = Iter(5)

# for i in x:
#     print(i)


# # # //////////////Generate //////////////////////

# def gen(n):
#     for i in range(n):
#         yield i

# x = gen(5)

# for i in x:
#     print(i)


# # //////////////Generate //////////////////////

# def gen(n):
#     for i in range(n):
#         print(f'Pause {i}')
#         yield i

# x = gen(5)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


# ////////////// Generate //////////////////////

# def gen():
#     yield 1
#     print('Pause 1')
#     yield 2
#     print('Pause 2')
#     yield 3
#     print('Pause 3')
#     yield 4

   
# x = gen()

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


# /////////// list //////////////

# x = [i for i in range(5)]

# print(x)


# # //////////  tuple ///////////////

# x = (i for i in range(5))

# print(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# # ////////// generator tuple ///////////////

# x = (i for i in range(5))

# print(x)

# y = []
# for n in x:
#     y.append(n)

# print(y)


# # //////////////////////////////////////

# def get_values():

#     yield 'Hello'
#     yield 'world'
#     yield 123


# def example_get_values():
#     gen = get_values()
#     print(gen)
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
  

# example_get_values()


# //////////////////////////////////////

# def get_values():

#     yield 'Hello'
#     yield 'world'
#     yield 123


# def example_get_values():   
    
#     for x in get_values():
#         print(x)  

# example_get_values()

# //////////////////////

# import time

# def my_generator(x=1):
#     while True:
#         yield x
#         x += 1

# gene = my_generator()
# print(type(gene))

# for i in gene:
#     print(i, end='')
#     time.sleep(0.5)


    
    

   
   
    









