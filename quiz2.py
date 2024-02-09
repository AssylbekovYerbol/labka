#1 Exercice
print (10>9)
#Ouput : "True"

#2 Exercise
print (10 == 9)
#Output : "False"

#3 Exercise
print(10 < 9)
#Output : "False"

#4 Exercise
print(bool("abc"))
#Output : "True"

#5 Exercise 
print(bool(0))
#Output : "False"

#Exercise 1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Exercise 2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#Exercise 3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#Exercise 4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#Exercise 5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#Exercise 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Exercise 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":   
   continue
  print(x)

#Exercise 3
for x in range(6):
  print(x)

#Exercise 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": 
   break
  print(x)

#Exercise 1
a = 50
b = 10
if a > b:
  print("Hello World")

#Exercise 2
a = 50
b = 10
if a != b:
  print("Hello World")

#Exercise 3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

#Exercise 4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

#Exercise 5
if a == b and c == d:
  print("Hello")

#Exercise 6
if a == b or c == d:
  print("Hello")

#Exercise 7
if 5 > 2:
 print("YES")

#Exercise 8
 a = 2
b = 5
print("YES") if a==b else print("NO")

#Exercise 9
a = 2
b = 50
c = 2
if a==c or b==c:
  print("YES")

#1 Exercise 
fruits = ["apple", "banana", "cherry"]
print(fruits[1]) 

#2 Exercise 
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#3 Exercise
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#4 Exercise
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#5 Exercise 
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#6 Exercise 
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#7 Exercise 
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#8 Exercise 
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#1 Exercise 
print(10 * 5)
#Multiplication symbol "*", the Output : 50

#2 Exercise
print(10/2)
#Division symbol "/", the Output : 5

#3 Exercise 
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#Membership operator "in" was used
  
#4 Exercise 
if 5 != 10:
  print("5 and 10 is not equal")
#Comparison operator "!=" was used
  
#5 Exercise 
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")
#Logical operator "or" was used
  
#Exercise 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
 print("Yes, apple is a fruit!")

#Exercise 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Exercise 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Exercise 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#Exercise 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#Exercise 1 
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Exercise 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Exercise 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Exercise 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Exercise 1
i = 1
while i < 6:
  print(i)
  i += 1

#Exercise 2
i = 1
while i < 6:
  if i == 3: 
   break
  i += 1

#Exercise 3
i = 0
while i < 6:
  i += 1
  if i == 3: 
   continue
  print(i)

#Exercise 4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")