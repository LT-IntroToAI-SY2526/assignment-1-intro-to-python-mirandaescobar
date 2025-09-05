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
Age in months: 192

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

Problem 6: To-Do List Manager (Lists & Functions)
Difficulty: ⭐⭐⭐⭐
Build a simple to-do list program with multiple functions.
Instructions:
Create these functions:

add_task(todo_list, task) - adds a task to the list
remove_task(todo_list, task) - removes a task from the list
show_tasks(todo_list) - displays all tasks with numbers
mark_complete(todo_list, task_number) - marks a task as complete by adding "[DONE]" to it

In your main program:

Start with an empty list
Add at least 3 tasks
Display the list
Mark one task as complete
Remove one task
Display the final list

Example Output:
Added: Buy groceries
Added: Study Python
Added: Call mom

To-Do List:
1. Buy groceries
2. Study Python
3. Call mom

Marked task 2 as complete

Removed: Call mom

Final To-Do List:
1. Buy groceries
2. Study Python [DONE]

Problem 7: Word Counter (Strings, Lists, Loops, Functions)
Difficulty: ⭐⭐⭐⭐⭐
Create a program that analyzes text and counts words.
Instructions:
Create these functions:

count_words(text) - returns the total number of words
find_longest_word(text) - returns the longest word
count_word_frequency(text, word) - returns how many times a specific word appears (case-insensitive)

In your main program:

Ask user for a sentence
Use all three functions to analyze the text
Display the results in a nice format

Example Input/Output:
Enter a sentence: The quick brown fox jumps over the lazy dog. The dog runs fast.

Text Analysis Results:
- Total words: 12
- Longest word: jumps
- How many times does 'the' appear? 2
- How many times does 'dog' appear? 2


Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
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


