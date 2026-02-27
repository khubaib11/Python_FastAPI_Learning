# --------------------
# Create And use module
# ---------------------
# from testModule1 import add

# result= add(10,11)
# print(result)



# ------------------
# 1 OS Module
# ------------------

# Working with Current Directory

# import os

# print(os.getcwd())  # Get Current Working Directory (CWD)
# os.chdir("..")      # Change directory to parent folder
# print(os.getcwd())



# Creating, Listing, and Deleting Directories

# os.mkdir("myfolder")      # Create a folder
# os.makedirs("myfolder/subfolder")  # Create nested folders
# print(os.listdir("."))    # List all files/folders in current directory
# os.rmdir("myfolder/subfolder")     # Remove empty folder
# os.removedirs("myfolder")          # Remove nested folders


# Working with Files / Paths
# print(os.path.exists("myfile.txt"))    # Check if file/folder exists
# print(os.path.isfile("myfile.txt"))    # Is it a file?
# print(os.path.isdir("myfolder"))       # Is it a folder?
# print(os.path.join("folder", "file.txt"))  # Join paths safely
# print(os.path.abspath("myfile.txt"))       # Absolute path of file



# Use os.environ
# it will store the the enviroment varable for operating system we use load env to safe this os.eniron

# main.py
# from dotenv import load_dotenv
# import os

# print(os.environ)
# load_dotenv()  # read .env file

# api_key = os.environ.get("API_KEY")
# db_url = os.environ.get("DB_URL")

# print(f"API Key: {api_key}")
# print(f"Database URL: {db_url}")



#Sys it is use for the python interpretator like if we need to stop the code we used it or find out which python version like that 


#Json Module

#use Dumps when we need to covert dict to json

# import json

# data = {
#     "name": "Khubaib",
#     "age": 22
# }

# json_string = json.dumps(data)

# print(json_string)
# print(type(json_string))


#use loads when we need to covert json string to dict
# import json

# json_string = '{"name": "Khubaib", "age": 22}'

# data = json.loads(json_string)

# print(data)
# print(type(data))


#datetime use to play with time and it formate like that

