# Assignment 1: AI-Generated Python Problems
# Name: Miranda Escobar

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class.
 I have some experience with I'm new to programming'.
   Can you create 5-7 practice problems that cover:
     > - Variables and basic data types
       > - Conditionals (if/elif/else) 
       > - Loops (for and while) 
       > - Functions 
       > - Basic list operations  
       > Make them progressively more challenging.
     Make sure each problem has clear instructions and example inputs/outputs.

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
 PROBLEM 1: Personal Information (Variables & Data Types)
Difficulty: ⭐
Create a program that stores and displays personal information using different data types.
Instructions:

Create variables for: name (string), age (integer), height in feet (float), is_student (boolean)
Print each piece of information with a descriptive label
Calculate and display age in months

Example Output:
Name: Alice
Age: 16 years
Height: 5.4 feet
Student Status: True
Age in months:192
"""
name = "Alice"
age = 16
height = 5.4
student_status = True
age_in_months = 12* age


"""

Problem 2: Simple Calculator (Variables, Input, Conditionals)
Difficulty: ⭐⭐
Build a basic calculator that performs one operation on two numbers.
Instructions:

Ask user for two numbers
Ask user to choose an operation (+, -, *, /)
Use if/elif/else to perform the correct operation
Display the result
Handle division by zero with an error message

Example Input/Output:
Enter first number: 10
Enter second number: 3
Choose operation (+, -, *, /): *
Result: 10.0 * 3.0 = 30.0
"""
first_num = int(input("Please input a number here:"))
second_num = int(input("Please input a second number here:"))
operation = input("Please choose an operation (+, -, *, /): ")
if operation == "+":
    result = first_num + second_num
elif operation == "-":
    result = first_num - second_num
elif operation == "*":
    result = first_num * second_num
elif operation == "/":
    result = first_num / second_num
   

"""

Problem 3: Number Classifier (Conditionals & Loops)
Difficulty: ⭐⭐
Write a program that classifies numbers based on their properties.
Instructions:

Ask the user how many numbers they want to enter
Use a for loop to get that many numbers from the user
For each number, determine and print if it's:

Positive, negative, or zero
Even or odd (use modulo operator %)


Keep count of how many positive numbers were entered

Example Input/Output:
How many numbers? 3
Enter number 1: 5
5 is positive and odd
Enter number 2: -4
-4 is negative and even
Enter number 3: 0
0 is zero and even
You entered 1 positive number(s)
"""
how_many_num = int(input("How many numbers do you want to enter?")) 
positive_count = 0 

for i in range (1, count +1):
    number = int(input(f"Enter number {i}:") )
    if number > 0:
        sign = "postive"
        positive_count += 1

    elif number < 0:
        sign = "negative"
    else :
        sign = "zero"
        if number % 2 ==0
        print (f "{}")
        


"""
Problem 4: Guess My Number (While Loops & Conditionals)
Difficulty: ⭐⭐⭐
Create a number guessing game using a while loop.
Instructions:

Set a secret number (you can hardcode it as 42 for now)
Use a while loop to keep asking for guesses until correct
Give hints: "Too high!" or "Too low!"
Count the number of attempts
Congratulate the user when they guess correctly

Example Output:
I'm thinking of a number between 1 and 100!
Enter your guess: 50
Too high!
Enter your guess: 25
Too low!
Enter your guess: 42
Congratulations! You got it in 3 attempts!

Problem 5: Grade Average Calculator (Functions & Lists)
Difficulty: ⭐⭐⭐
Create functions to work with a list of grades.
Instructions:

Create a function calculate_average(grades) that returns the average of a list of grades
Create a function get_letter_grade(average) that returns a letter grade:

A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60


In your main program:

Create a list with at least 5 test grades
Use your functions to calculate and display the average and letter grade



Example Output:
Grades: [85, 92, 78, 88, 95]
Average: 87.6
Letter Grade: B
"""
"""


"""











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
# Add your tests here

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


