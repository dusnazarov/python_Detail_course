# nums = [1, 2, 3]

# # print(dir(nums))

# iter_nums = nums.__iter__()

# print(iter_nums)

# print(dir(iter_nums))

# # ////////////////////////////
# class MyRange:

#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         current = self.start
#         self.start += 1
#         return current
        
# nums = MyRange(1, 10)
# # print(next(nums))
# # print(next(nums))
# # print(next(nums))
# # print(next(nums))
# # print(next(nums))

# for num in nums:
#     print(num)

# # ///////// Generation ///////////////////////////

# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1

# nums = my_range(1, 10)

# # print(next(nums))
# # print(next(nums))
# # print(next(nums))

# for num in nums:
#     print(num)

#////////////////////////////////////
# class Sentence:

#     def __init__(self, sentence):
#         self.sentence = sentence
#         self.index = 0
#         self.words = self.sentence.split()        

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index >= len(self.words):
#             raise StopIteration
        
#         index = self.index
#         self.index += 1
#         return self.words[index]

# my_sentence = Sentence('This is a test')

# for word in my_sentence:
#     print(word)

# ///////////// generation ///////////////////////

# def sentence(sentence):
#     for word in sentence.split():
#         yield word

# my_sentence = sentence('This is a test')


# for i in my_sentence:
#     print(i)
        

    






