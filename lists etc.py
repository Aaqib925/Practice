# there are three types...lists, tuples and sets....for list [] , for tuples () , and for sets {}
# lists are mutable are the tuples are immutable....that means nothing can be added or changed in the tuples or sets

#LISTS
# course = ["Maths", "Chemistry", "Physics", "CompSci"]
#print(course)
#print(course[0:3])  #this is for the range
#print(len(course))

# to add something in the list we can use the keyword of append, insert and expand...all of them are used according to the condition

# course.append("Art")  # append will add the word in the end of the list...
# print(course)

# but if we want to add something on the particular index of the list...we can use the insert keyword

# course.insert(1, "Art") # this syntax shows k hamen pehle index dalna ha then insert hoga
# print(course)

# course = ["Maths", "Chemistry", "Physics", "CompSci"]
# course_2 = ["Arts", "Education"]
#
# course.insert(0, course_2)   # this function adds the second list in the first list....and it is not desired output
# print(course)

# to add the second list to the first list without any problem we used the third option of extend

# course = ["Maths", "Chemistry", "Physics", "CompSci"]
# course_2 = ["Arts", "Education"]
#
# course.extend(course_2)    by this you can actually add the things into the list
# print(course)

# Method to remove anything from the lists
# course = ["Maths", "Chemistry", "Physics", "CompSci"]
#
# course.remove("Maths")
# print(course)

# course = ["Maths", "Chemistry", "Physics", "CompSci"]
# course.pop()   #agar mn koi index nahi dunga to last wala pop out hojaega otherwise popping can also be done by using index
# print(course)

# if we want to print the popped value of the list

# course = ["Maths", "Chemistry", "Physics", "CompSci"]
#
# removed_thing = course.pop()
#
# print("THe popped thing from the list is: " + removed_thing)

# to print the the list in the reverse format

# course = ["Maths", "Chemistry", "Physics", "CompSci"]
#
# course.reverse()
# print(course)

# the way to sort the list in alphabet wise or ascending or descending wise the keyword sort() is used
# course = ["Maths", "Chemistry", "Physics", "CompSci"]
#
# course.sort()
# print(course)
#
# num = [2, 3, 1, 8, 5]
# num.sort()
# print(num)

# if you want to reverse your sorted list in descending terms then

# num = [1, 34, 45, 22, 100]
#
# num.sort(reverse=True)
# print(num)

# another method to sort out the list in such a way the the original one doesn't changes

# course = ["Maths", "Chemistry", "Physics", "CompSci"]
#
# sorted_course = sorted(course)
#
# print(sorted_course)

# for the minimun we use min() for maximum we use max() and for the sum of the numbers in the list we use sum()

# num = [1, 3, 45, 33, 66]
#
# print(min(num))
# print(max(num))
# print(sum(num))

#course = ["Maths", "Chemistry", "Physics", "CompSci"]
#print("The Index of the required data is: " + str(course.index("CompSci")))

# conditionals
#course = ["Maths", "Chemistry", "Physics", "CompSci"]
#print("Arts" in course)

# course = ["Maths", "Chemistry", "Physics", "CompSci"]
# for item in course:
#     print(item)

# course = ["Maths", "Chemistry", "Physics", "CompSci"]
# for index, item in enumerate(course):
#     print(index, item)

# converting the list to get the single String and getting back the list
# course = ["Maths", "Chemistry", "Physics", "CompSci"]
#
# course_str = ", ".join(course)    # this will convert the list into single string using join keyword
#
# print(course_str)

# course = ["Maths", "Chemistry", "Physics", "CompSci"]
#
# course_str = " - ".join(course)
# print(course_str)
#
# new_list = course_str.split(" - ")
#
# print(new_list)

# course = ["Maths", "Chemistry", "Physics", "CompSci"]   # lists are mutable...it means that there data can be changed
# course2 = course
#
# print(course)
# print(course2)
#
# course[0] = "Arts"   # also course.append("Arts") or course.insert(0, "Arts")
#
# print(course)
# print(course2)

# tuples in python are represented by () round brackets are also immutable...means nothing can be added into them

# tuple_1 = course = ("Maths", "Chemistry", "Physics", "CompSci")
# tuple_2 = tuple_1
#
# print(tuple_1)
# print(tuple_2)
#
# # tuple_1[0] = "Arts"   # it means that data in tuple cannot be changed
#
# print(tuple_1)
# print(tuple_2)

# sets are the values that are unordered and no duplicates and uses {}

# course = {"Maths", "Chemistry", "Physics", "CompSci", "Arts"}
# print("Maths" in course)   #everytime the the set is executed...the order or print changess

# course = {"Maths", "Chemistry", "Physics", "CompSci"}
#
# print("Maths" in course)

# course = {"Maths", "Chemistry", "Physics", "CompSci"}
# course2 = {"Maths", "Biology", "Statics", "CompSci"}

# print(course.union(course2))
# print(course.difference(course2))
# print(course.intersection(course2))

# Also...{} can never be empty...it is called dictionary