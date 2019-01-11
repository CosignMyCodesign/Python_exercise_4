# Tuples are like lists, but are immutable. They can't be modified once defined. However, finding values in a tuple is faster than in a list.

# 1. Create a tuple named zoo that contains your favorite animals.
zoo = ("monkey", "liger", "quokka", "elephant")

# 2. Find one of your animals using the .index(value) method on the tuple.
print("3rd animal =", zoo[2])
# 3. Determine if an animal is in your tuple by using value in tuple.
if "elephant" in zoo:
  print("Why yes, there is an elephant in your zoo")
else:
  print("No, but there should be")
# 4. Create a variable for each of the animals in your tuple with this cool feature of Python.
(monkey, liger, quokka, elephant) = zoo
print(monkey)
# 5. Convert your tuple into a list.
zoo_list = list(zoo)
print(zoo_list)
# 6. Use extend() to add three more animals to your zoo.
zoo_list.extend(["gorilla", "dolphin", "penguin"])
# 7. Convert the list back into a tuple.
zoo = tuple(zoo_list)
print(zoo)