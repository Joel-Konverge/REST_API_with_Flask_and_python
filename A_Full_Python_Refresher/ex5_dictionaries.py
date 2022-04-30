#This coding exercise has three parts. See them outlined in detail in the coding exercise, as comments.
# Create a dictionary variable, called student
# Modify a variable, grades, so it contains the value of a dictionary's key.
# Implement a function calculating a total average grade for a class of students.


# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.



from itertools import count


student={'name':"Jose",'school':"Computing",'grades':(66,77,88)}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.

def average_grade(data):
    grades=data['grades']
    return sum(grades)/len(grades)

print(average_grade(student))


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list

student_list=[{'name':"Jose",'school':"Computing",'grades':(1,2,3)},{'name':"Tom",'school':"Computing",'grades':(0,0,0)},{'name':"Kim",'school':"Computing",'grades':(2,10,55)}]

def average_grade_all_students(student_list):
    tot_grade=count=0
    for i in student_list:
        tot_grade+=sum(i['grades'])
        count+=1
    return (tot_grade/len(student_list[0]['grades']))/count

print(average_grade_all_students(student_list))