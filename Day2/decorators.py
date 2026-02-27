# ===========
# Decorators
# ===========

# A decorator is a function that adds extra functionality to another function without changing the original function’s code.


# Decorator function
# def my_decorator(func):
#     def wrapper(*args, **kwargs):  # accept any arguments
#         print("Before calling the function")
#         func(*args, **kwargs)       # call the original function with same arguments
#         print("After calling the function")
#     return wrapper

# # Original function
# @my_decorator
# def say_hello(no):
#     print("Hello!", no)

# # Decorate the function
# say_hello = my_decorator(say_hello)

# # Call the decorated function
# say_hello(10)


# say_hello(10)



#Class based Decorators
#like __call__ is used for clased based decorators 
# class MyDecorator:
#     def __init__(self, func):
#         self.func = func  # store the original function

#     def __call__(self, *args, **kwargs):
#         print("Before calling function")
#         result = self.func(*args, **kwargs)
#         print("After calling function")
#         return result

# # Use as decorator
# @MyDecorator
# def say_hello(name):
#     print(f"Hello {name}!")

# # Call the decorated function
# say_hello("Khubaib")

# print(type(say_hello))