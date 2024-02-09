# import json
# # some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'
# # parse x:
# y = json.loads(x)
# # the result is a Python dictionary:
# print(y["age"])

# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# # convert into JSON:
# y = json.dumps(x)
# # the result is a JSON string:
# print(y)

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# #print(json.dumps(x, indent=2))
# #print(json.dumps(x, indent=4, separators=(". ", " = ")))
# print(json.dumps(x, indent=4, sort_keys=True))

# import re
# #Check if the string starts with "The" and ends with "Spain":
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

# import re

# txt = "The rain in Spain"

# #Find all lower case characters alphabetically between "a" and "m":
# x = re.findall("[a-m]", txt)
# print(x)


# import re
# txt = "That will be 59 dollars"

# #Find all digit characters:

# x = re.findall("\d", txt)
# print(x)

# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start())

# import re

# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)


# try:
#   print(x)
# except:
#   print("An exception occurred")

# x = ('Hello')
# try:
#   print(x)
# except :
#   print("Variable x is not defined")
# else:
#   print("Something else went wrong")


# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# #x = -1
# #if x < 0:
#   #raise Exception("Sorry, no numbers below zero")

# #x = ('Hello')
# #if not type(x) is int:
#   #raise TypeError("Only integers are allowed")
# #print(x)

# #Input
# username = input("Enter username:")
# print("Username is: " + username)

# price = 49
# txt = "The price is {} dollars"
# print(txt.format(price))

# price = 49
# txt = "The price is {:.2f} dollars"
# print(txt.format(price))

# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# myorder = "I have a {carname}, it is a {model}."
# print(myorder.format(carname = "Ford", model = "Mustang"))

# #f = open("demofile.txt", "r")
# #print(f.read())

# #f = open("D:\\myfiles\welcome.txt", "r")
# #print(f.read())

# #f = open("demofile.txt", "r")
# #print(f.read(5))

# #f = open("demofile.txt", "r")
# #print(f.readline())

# #f = open("demofile.txt", "r")
# #for x in f:
#   #print(x)

# #f = open("demofile.txt", "r")
# #print(f.readline())
# #f.close()


# #f = open("demofile2.txt", "a")
# #f.write("Now the file has more content!")
# #f.close()

# #open and read the file after the appending:
# #f = open("demofile2.txt", "r")
# #print(f.read())

# #f = open("demofile3.txt", "w")
# #f.write("Woops! I have deleted the content!")
# #f.close()

# #open and read the file after the overwriting:
# #f = open("demofile3.txt", "r")
# #print(f.read())

# #import os
# #os.remove("demofile.txt")

# #import os
# #if os.path.exists("demofile.txt"):
#   #os.remove("demofile.txt")
# #else:
#   #print("The file does not exist")

# #import os
# #os.rmdir("myfolder")

# import matplotlib
# print(matplotlib.__version__)



























































































































































































































































































































