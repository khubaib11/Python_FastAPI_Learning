# --------------
# #Iterator
# --------------


# it is simple object that have two methods iter (return itself )and next (return next value)
# my_list = [10, 20, 30]
# it = iter(my_list)  # convert list to iterator

# print(next(it))  # 10
# print(next(it))  # 20
# print(next(it))  # 30
# next(it) now → StopIteration  
# print(type(it))
# for i in it:
#     print(i)


# -------------
# #Generators
# -------------

# def generators():
#     print("h1")
#     yield 
#     print("h2")
#     yield 
#     print("h3")
#     yield 


# gen =generators()

# next(gen)
# next(gen)
# next(gen)
