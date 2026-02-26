# ------------------------
# lambda function 
# --------------------------
# is a small, anonymous function in Python.
# lambda parameter : return 

# add= lambda x,y : x+y

# print(add(10,11))


# print(
# (lambda x: x + 1)(2)
# )

# #closure
# def outerFunc():
#     x = 10
#     def innerFunc(y):
#         return x + y
#     return innerFunc   # <--- return the inner function

# # Create the closure
# outObj = outerFunc()

# # Call the inner function via outObj
# print(outObj(10))   # 10 + 10 = 20


# -----------------
# Map Functions
# -----------------


#it is used for all iteratable  like list tuple and dict.items()
# list1=[1,2,3,4]
# ans=list(map(lambda x: x**3,list1))
# print(ans)


# -----------------
# Filter Functions
# -----------------

#It selects items from an iterable that meet a certain condition
# list2 = [4,3,1,5,2,0,10]
# ans=list(filter(lambda x : x % 2 == 0,list2))
# print(ans)


# -----------------
# Reducer Functions
# -----------------

#) that reduces a collection of items to a single value.
# from functools import reduce

# list3 = [19, 20, 11]

# ans = reduce(lambda acc, cur: acc - cur, list3, 100)  # 100 is initializer
# print(ans)  # 50

