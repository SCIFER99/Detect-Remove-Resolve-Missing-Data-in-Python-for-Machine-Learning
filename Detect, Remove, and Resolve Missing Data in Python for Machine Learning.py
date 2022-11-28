# By: Tim Tarver also known as CryptoKeyPlayer
# This script is created to detect, remove and resolve
# data missing from any machine learning project.

# Best viewed in Jupyter Notebooks; one method in each cell. 

import openpyxl
import pandas

# Lets begin with a constructor method with a variable we
# will use throughout the script.

def __init__(self, data1, data2, students):

    self.data1 = data1
    self.data2 = data2
    self.students = students
    return data1, data2, students

# Now, we continue with a method to open the provided
# excel file.

def open_excel_file():

    students = pandas.read_excel("students.xlsx")
    return students

print(open_excel_file())

# Next, we begin building a method that
# can detect which state has a "NaN" located under "State" label
# then print out only the lines with "NaN" under "State".

def missing_value_detector():

    students = pandas.read_excel("students.xlsx")
    data1 = students['State'].isnull()
    data2 = students[data1]
    return data1, data2

print(missing_value_detector())

# Then, we begin to demonstrate how to remove the "NaN" value from
# the "State" and "Zip" data and return the remaining data.

def remove_all_missing_values():

    students = pandas.read_excel("students.xlsx")
    data3 = students.dropna()

    # Each line below this should go in its own Jupyter Notebook cell.
    students = students.dropna(subset = ['State', 'Zip'], how = 'all')
    
    # To remove Minor, Age, State and Zip
    students = students.dropna(axis = 1)
    
    # To remove all "NaN" from the whole data set.
    students = students.dropna(axis = 1, thresh = 10)
    
    return data3, students, students, students

print(remove_all_missing_values())

# Henceforth, we move on to the next method of resolving missing data.

def resolve_all_missing_data():

    students = pandas.read_excel("students.xlsx")

    # First cell
    students = students.fillna({'Gender': 'Female'})

    # Second cell
    students = students.fillna({'Age': students['Age'].median()})
    
    # Third cell
    mask = (students['City'] == 'Granger') & (students['State'] == 'IN')
    
    # Fourth cell
    students = students.loc[mask, :]

    # Fifth cell
    # students = students.loc[mask, 'Zip'] = 46530

    # Sixth cell
    mask = (students['City'] == 'Niles') & (students['State'] == 'MI')
    # students = students.loc[mask, 'Zip'] = 49120
    return students, students, students, students

print(resolve_all_missing_data())
    
