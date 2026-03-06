Question 1 - pseudo_range(n)

Convert the following pseudocode into Python inside the pseudo_range(n) function:

FOR i FROM 1 TO n INCLUSIVE DO
PRINT i
END FOR


The function must print the numbers from 1 to n, each on a new line.
Question 2 - do_not_panic(n)

This function must:


Compute the sum of numbers from 1 to n


Return True if the sum is even


Return False if the sum is odd


The provided code contains syntax errors and logical errors.
Fix the loop, the arithmetic, and the return condition.
Question 3 - countdown_even(n)

Fix the function so that it:


Uses a loop


Prints all even numbers from n down to 0 (inclusive)


Prints each number on its own line


Correctly decreases the value of n each iteration


The starter version contains broken logic and broken operators — repair it properly.
Question 4 - check_password(pass)

Write a function check_password(password: str) -> str that returns a password strength rating based on the rules below:



Condition
Required Return Value




Password is empty
"Invalid"


Password length is less than 6 characters
"Weak"


Contains letters and numbers

"Medium"


Contains letters, numbers, and symbols (!@#$%^&*)
"Strong"



You must complete the missing conditions and correctly implement:


has_letter


has_number


has_symbol


Use Python tools such as isalpha(), isdigit(), and membership checks (in '!@#$%^&*').
Question 5 - reverse_words(sentence)

Complete the function so that it:

Reverses the order of words (NOT the letters)


Input:  "This is  a test"
Output: "test a is This"


Return the reversed sentence.
Your Goal

Fix all functions in fundamentals.py so that:


The code is valid Python


Each function behaves according to the rules above


All unit tests pass successfully


Good luck — and remember to think carefully about your loops, conditions, and syntax!