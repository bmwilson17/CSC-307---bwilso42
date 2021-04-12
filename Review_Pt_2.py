#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = "Tom"
student_1 = "Tom"
student_2 = "Jerry"

if(name == "Yongcheng"):
    print("instructor")
elif(name == "Tom" or name == "Jerry"):
    print("student")
else:
    print("cannot identify")


# In[2]:


# A new student called "Quacker"

name = "Yongcheng"
student_1 = "Tom"
student_2 = "Jerry"
student_3 = "Quacker"

if(name == "Yongcheng"):
    print("instructor")
elif(name == "Tom" or name == "Jerry" or name == "Quacker"):
    print("student")
else:
    print("cannot identify")


# In[3]:


# Use a list
name = "Tom"
student_list = ["Tom", "Jerry", "Quacker"]

if(name == "Yongcheng"):
    print("instructor")
elif(name in student_list):
    print("student")
else:
    print("cannot identify")


# In[4]:


# Multiple instructors
name = "Yongcheng"
student_list = ["Tom", "Jerry", "Quacker"]
instructor_list = ["Yongcheng", "Kevin"]

if(name in instructor_list):
    print("instructor")
elif(name in student_list):
    print("student")
else:
    print("cannot identify")
    



# In[5]:


# list: ordered
food_list = ["ice_cream", "apple", "donut"]
print(food_list[0])
print(food_list[2])
print(food_list[-1])
print(food_list[0:2])
print(food_list[0:1])
print(food_list[-2:])
print(food_list[-2:-1])


# In[6]:


# Strings are also indexed
s = "Hello, World"
print(s[0:2])
print(s[-3:-1])


# In[7]:


# list: changeable
food_list = ["ice_cream", "apple", "donut"]
food_list[0] = "cake"
print(food_list[0])
print(food_list)


# In[8]:


# list: check if exists
food_list = ["ice_cream", "apple", "donut"]
if("apple" in food_list):
    print("Yes!")


# In[9]:


# list: length
food_list = ["ice_cream", "apple", "donut"]
print(len(food_list))


# In[10]:


# list methods
food_list = ["ice_cream", "apple", "donut"]
food_list.append("cake")
print(food_list)

food_list.insert(0, "hotdog")
print(food_list)

food_list.remove("cake")
print(food_list)

food_list.pop(0)
print(food_list)

food_list.clear()
print(food_list)


# In[11]:


# list copy: wrong
food_list = ["ice_cream", "apple", "donut"]
print(food_list)

food_list2 = food_list
food_list2[0] = "hotdog"
print(food_list2)
print(food_list)


# In[12]:


# list copy: correct
food_list = ["ice_cream", "apple", "donut"]
print(food_list)

food_list2 = food_list.copy()
food_list2[0] = "hotdog"
print(food_list2)
print(food_list)


# In[13]:


# combine two lists
food_list = ["ice_cream", "apple", "donut"]
food_list2 = ["hotdog", "strawberry", "cake"]
food_list.extend(food_list2)
print(food_list)


# In[14]:


# element count
food_list = ["ice_cream", "apple", "donut", "donut"]
print(food_list.count("donut"))


# In[15]:


# set: no duplicate members
food_set ={"ice_cream", "apple", "donut"}
print(food_set)
print("\n")
food_set ={"ice_cream", "apple", "donut", "donut"}
print(food_set)


# In[16]:


# set: element existance and set length
if("apple" in food_set):
    print("Yes")

print(len(food_set))


# In[17]:


# set: unordered
print(food_set[0])


# In[18]:


# set: union and intersection

my_favorite_food = {"ice_cream", "donut", "apple"}
your_favorite_food = {"pizza", "ice_cream", "steak"}

both_like = my_favorite_food.intersection(your_favorite_food)
print(both_like)

both_like = your_favorite_food.intersection(my_favorite_food)
print(both_like)

either_like = my_favorite_food.union(your_favorite_food)
print(either_like)


# In[19]:


# tuple: ordered
food_tuple = ("ice_cream", "apple", "donut")
print(food_tuple[0])


# In[20]:


food_tuple = ("ice_cream", "apple", "donut")
food_tuple[0] = "hotdog"
print(food_tuple)


# In[21]:


# one-element tuple
food_tuple = ("hotdog", )
print(food_tuple)


# In[22]:


# dictionary: key-value pairs

working_addr_dict = {
    "Yongcheng": "Cal Poly SLO",
    "Kevin": "LA"
}

addr = working_addr_dict["Yongcheng"]
print(addr)


# In[23]:


# dictionary: commonly used methods
working_addr_dict = {
    "Yongcheng": "Cal Poly",
    "Kevin": "LA"
}

print(working_addr_dict.keys())
print(working_addr_dict.values())
print(working_addr_dict.items())


# In[24]:


# dictionary: traverse the keys
working_addr_dict = {
    "Yongcheng": "Cal Poly",
    "Kevin": "LA"
}

for key in working_addr_dict.keys():
    print(key)


# In[25]:


# dictionary: traverse the values
working_addr_dict = {
    "Yongcheng": "Cal Poly",
    "Kevin": "LA"
}

for value in working_addr_dict.values():
    print(value)


# In[26]:


# dictionary: traverse the keys and values
working_addr_dict = {
    "Yongcheng": "Cal Poly",
    "Kevin": "LA"
}

for key, value in working_addr_dict.items():
    print(key, value)
    print("\n")


# In[27]:


# convert data structure
tuple1 = ("apple", "banana")
list1 = list(tuple1)
print(list1)


# In[28]:


# tuple ()
# list []
# set {}
# dictionary {key: value}


# In[29]:


# Code Reuse: function


grade = 75

if(grade >= 93):
    lgrade = "A"
    sgrade = 4.0
elif(grade >= 90):
    lgrade = "A-"
    sgrade = 3.7
elif(grade >= 87):
    lgrade = "B+"
    sgrade = 3.3
elif(grade >= 83):
    lgrade = "B"
    sgrade = 3.0
elif(grade >= 80):
    lgrade = "B-"
    sgrade = 2.7
elif(grade >= 77):
    lgrade = "C+"
    sgrade = 2.3
elif(grade >= 73):
    lgrade = "C"
    sgrade = 2.0
elif(grade >= 70):
    lgrade = "C-"
    sgrade = 1.7
elif(grade >= 67):
    lgrade = "D+"
    sgrade = 1.3
elif(grade >= 63):
    lgrade = "D"
    sgrade = 1.0
elif(grade >= 60):
    lgrade = "D-"
    sgrade = 0.7
else:
    lgrade = "F"
    sgrade = 0

print(lgrade, sgrade)


# In[30]:


# what about the following code:



# for student_name in class_1:
#     grade = get_student_grade(student_name)
#     if(grade > 93):
#         lgrade = A
#         sgrade = 4.0
# ......
# for student_name in class_2:
#     grade = get_student_grade(student_name)
#     if(grade > 93):
#         lgrade = A
#         sgrade = 4.0
# ......

# We can use a function to reuse the code


# In[31]:


# Code Reuse: function
def gradeCalculator(grade):
    if(grade >= 93):
        lgrade = "A"
        sgrade = 4.0
    elif(grade >= 90):
        lgrade = "A-"
        sgrade = 3.7
    elif(grade >= 87):
        lgrade = "B+"
        sgrade = 3.3
    elif(grade >= 83):
        lgrade = "B"
        sgrade = 3.0
    elif(grade >= 80):
        lgrade = "B-"
        sgrade = 2.7
    elif(grade >= 77):
        lgrade = "C+"
        sgrade = 2.3
    elif(grade >= 73):
        lgrade = "C"
        sgrade = 2.0
    elif(grade >= 70):
        lgrade = "C-"
        sgrade = 1.7
    elif(grade >= 67):
        lgrade = "D+"
        sgrade = 1.3
    elif(grade >= 63):
        lgrade = "D"
        sgrade = 1.0
    elif(grade >= 60):
        lgrade = "D-"
        sgrade = 0.7
    else:
        lgrade = "F"
        sgrade = 0
    
    return lgrade, sgrade


# In[32]:


grade = 75
lgrade, sgrade = gradeCalculator(grade)
print(lgrade, sgrade)


# In[33]:


# def gradeCalculator(grade):
#     if(grade > 93):
#         lgrade = A
#         sgrade = 4.0
# ......



# for student_name in class_1:
#     grade = get_student_grade(student_name)
#     lgrade, sgrade = gradeCalculator(grade)

# for student_name in class_2:
#     grade = get_student_grade(student_name)
#     lgrade, sgrade = gradeCalculator(grade)


# In[34]:


# Code reuse: import packages/modules
# To calculate square root...
# src: https://stackoverflow.com/questions/3047012/how-to-perform-square-root-without-using-math-module/3047046

def sqrt(x):
    last_guess= x/2.0
    while True:
        guess= (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .000001: # example threshold
            return guess
        last_guess= guess


# In[35]:


print(sqrt(2))


# In[36]:


# However, you can simply use the math module
import math
print(math.sqrt(2))

