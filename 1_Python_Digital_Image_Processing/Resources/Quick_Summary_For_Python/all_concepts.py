"""
COMPREHENSIVE PYTHON BASICS PROGRAM
This file contains examples of fundamental Python concepts
"""

# =============================================================================
# 1. VARIABLES AND BASIC DATA TYPES
# =============================================================================

print("=== 1. VARIABLES AND DATA TYPES ===")

# Integers (int)
age = 25
birth_year = 1998

# Floats (float)
height = 1.75
temperature = 36.5

# Strings (str)
name = "Maria"
last_name = 'Gonzalez'
message = """This is a
multi-line message"""

# Booleans (bool)
is_student = True
has_job = False

# None (null value)
empty_value = None

print(f"Name: {name}, Age: {age}, Height: {height}")
print(f"Is student? {is_student}")

# =============================================================================
# 2. OPERATORS
# =============================================================================

print("\n=== 2. OPERATORS ===")

# Arithmetic operators
a = 10
b = 3

sum_result = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulo = a % b
exponent = a ** b

print(f"Sum: {a} + {b} = {sum_result}")
print(f"Division: {a} / {b} = {division:.2f}")
print(f"Exponent: {a} ** {b} = {exponent}")

# Comparison operators
print(f"{a} > {b}: {a > b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")

# Logical operators
x = True
y = False

print(f"x AND y: {x and y}")
print(f"x OR y: {x or y}")
print(f"NOT x: {not x}")

# =============================================================================
# 3. DATA STRUCTURES
# =============================================================================

print("\n=== 3. DATA STRUCTURES ===")

# Lists (mutable, ordered)
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", True, 3.14]

print(f"Fruits list: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# List methods
fruits.append("mango")  # Add element
fruits.remove("banana") # Remove element
fruits.sort()           # Sort list
print(f"Sorted fruits: {fruits}")

# Tuples (immutable, ordered)
coordinates = (4, 5)
colors = ("red", "green", "blue")
print(f"Coordinates: {coordinates}")
print(f"First color: {colors[0]}")

# Dictionaries (key-value pairs)
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_employed": True
}
print(f"Person dictionary: {person}")
print(f"Person's name: {person['name']}")

# Sets (unordered, unique elements)
unique_numbers = {1, 2, 3, 3, 4, 4, 5}
print(f"Unique numbers: {unique_numbers}")

# =============================================================================
# 4. CONTROL FLOW
# =============================================================================

print("\n=== 4. CONTROL FLOW ===")

# If-elif-else statements
grade = 85

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# For loops
print("\n--- For Loops ---")
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

print("\nIterating through list:")
for fruit in fruits:
    print(f"Fruit: {fruit}")

# While loops
print("\n--- While Loop ---")
counter = 5
while counter > 0:
    print(f"Countdown: {counter}")
    counter -= 1

# =============================================================================
# 5. FUNCTIONS
# =============================================================================

print("\n=== 5. FUNCTIONS ===")

# Basic function
def greet():
    print("Hello, World!")

# Function with parameters and return value
def add_numbers(a, b):
    """This function adds two numbers and returns the result"""
    return a + b

# Function with default parameters
def introduce(name, age=25):
    return f"My name is {name} and I'm {age} years old"

# Calling functions
greet()
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")
print(introduce("Alice"))
print(introduce("Bob", 30))

# =============================================================================
# 6. STRING MANIPULATION
# =============================================================================

print("\n=== 6. STRING MANIPULATION ===")

text = "Hello Python World"

# String methods
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")
print(f"Length: {len(text)}")
print(f"Replace: {text.replace('Python', 'Amazing')}")
print(f"Split: {text.split()}")
print(f"Contains 'Python': {'Python' in text}")

# String formatting
name = "Carlos"
age = 28
formatted_string = f"{name} is {age} years old"
print(f"Formatted: {formatted_string}")

# =============================================================================
# 7. LIST COMPREHENSIONS
# =============================================================================

print("\n=== 7. LIST COMPREHENSIONS ===")

# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares (traditional): {squares}")

# Using list comprehension
squares_comp = [i ** 2 for i in range(1, 6)]
print(f"Squares (comprehension): {squares_comp}")

# List comprehension with condition
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(f"Even squares: {even_squares}")

# =============================================================================
# 8. ERROR HANDLING
# =============================================================================

print("\n=== 8. ERROR HANDLING ===")

# Try-except block
try:
    number = int("not_a_number")
    result = 10 / 0
except ValueError as e:
    print(f"ValueError occurred: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred!")
finally:
    print("This always executes")

# =============================================================================
# 9. FILE HANDLING
# =============================================================================

print("\n=== 9. FILE HANDLING ===")

# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, this is a test file!\n")
    file.write("Python file handling example.\n")

print("File 'example.txt' created and written successfully!")

# Reading from a file
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("File not found!")

# =============================================================================
# 10. CLASSES AND OBJECTS
# =============================================================================

print("\n=== 10. CLASSES AND OBJECTS ===")

class Person:
    # Class attribute
    species = "Homo sapiens"
    
    # Constructor
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    # Another method
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! Now I'm {self.age} years old"

# Creating objects
person1 = Person("Anna", 25)
person2 = Person("Tom", 30)

print(person1.introduce())
print(person2.introduce())
print(person1.have_birthday())
print(f"Both are {Person.species}")

# =============================================================================
# 11. MODULES
# =============================================================================

print("\n=== 11. MODULES ===")

# Importing built-in modules
import math
import datetime
import random

# Using imported modules
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi value: {math.pi:.2f}")
print(f"Current date: {datetime.datetime.now()}")
print(f"Random number: {random.randint(1, 100)}")

# =============================================================================
# 12. PRACTICAL EXAMPLE
# =============================================================================

print("\n=== 12. PRACTICAL EXAMPLE ===")

def calculate_grade_statistics(grades):
    """Calculate statistics for a list of grades"""
    if not grades:
        return "No grades provided"
    
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    # Determine overall performance
    if average >= 90:
        performance = "Excellent"
    elif average >= 80:
        performance = "Good"
    elif average >= 70:
        performance = "Average"
    else:
        performance = "Needs improvement"
    
    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "performance": performance
    }

# Example usage
student_grades = [85, 92, 78, 90, 88]
stats = calculate_grade_statistics(student_grades)

print(f"Grades: {student_grades}")
print(f"Average: {stats['average']:.2f}")
print(f"Highest: {stats['highest']}")
print(f"Lowest: {stats['lowest']}")
print(f"Performance: {stats['performance']}")

print("\n" + "="*50)
print("PROGRAM COMPLETED SUCCESSFULLY!")
print("You've learned the fundamental concepts of Python!")
print("="*50)
