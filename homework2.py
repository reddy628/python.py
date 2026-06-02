Here are the complete solutions, explanations, and code blocks for your Python worksheet.
## 1. Operator Selection

* 10 * 3 = 30 (Multiplication)
* 10 / 3 = 3.33... (Float Division)
* 10 // 3 = 3 (Floor Division / Integer Division)
* 10 % 3 = 1 (Modulo / Remainder)
* 2 ** 8 = 256 (Exponent / Power)
* 5 / 0 = ??? (ZeroDivisionError)
* 7 ** 0 = 1 (Power of 0)

------------------------------
## 2. Type Conversion — Fix the Bugs## Bug 1 Fixed Code:

age1 = int(input('Your age: '))age2 = int(input('Father age: '))
print('Sum of ages:', age1 + age2)

## Bug 2 Explanation & Fix:

* Why is there an error? TypeError occurs because Python cannot implicitly add an integer (a) to a string (c). It does not know whether to perform math or text concatenation.
* Fixed code:

a = 10c = 'Romesh'
print(str(a) + c)

------------------------------
## 3. Comparison & Logical Operators — Predict the Output

| Expression | Your Prediction / Actual Output |
|---|---|
| 10 == 10 | True |
| 10 != 10 | False |
| 10 > 20 | False |
| 10 <= 10 | True |
| True and False | False |
| True or False | True |
| not True | False |
| False and True and True and True | False |
| True or False or False or False | True |
| not (True and False) | True |

## Short circuit question:

* Answer: 1 condition.
* Explanation: Python evaluates the very first False. Because it uses the and operator, the entire result must be false, so it stops checking immediately.

------------------------------
## 4. Conditional Statements — Write the Code## Part A: Scenario Code## Scenario 1:

num = int(input("Enter a number: "))if num > 0:
    print('Positive')elif num < 0:
    print('Negative')else:
    print('Zero')

## Scenario 2:

marks = int(input("Enter marks (0-100): "))if marks >= 90:
    print("A")elif marks >= 75:
    print("B")elif marks >= 60:
    print("C")elif marks >= 40:
    print("D")else:
    print("Fail")

## Part B: Questions

* Q1. In an if/elif/else block, how many blocks can execute at most? One block.
* Q2. What is indentation and why does Python require it? Indentation is the blank space (usually 4 spaces or 1 tab) at the beginning of a code line. Python requires it to define code blocks and variable scopes.
* Q3. Is else mandatory? Can you have if without else? No, it is not mandatory. You can use an if statement completely on its own.

------------------------------
## 5. For Loops — Trace & Write## Part A: Output Predictions

* Loop 1 Output:
1
2
3
4
5
* Loop 2 Output:
0
5
10
15
* Loop 3 Output:
10
8
6
4
2

## Part B: Write the Loop Code## 1. Even numbers 2 to 20:

for i in range(2, 21, 2):
    print(i)

## 2. Numbers 100 down to 10:

for i in range(100, 9, -10):
    print(i)

## 3. Multiplication table of 7:

for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

## Part C: Loop Questions

* Q1. What is range(5) equivalent to? range(0, 5, 1). Start is 0, end is 5 (exclusive), and step is 1.
* Q2. What is an infinite loop and how do you avoid it? A loop that never stops running because its condition always remains true. Avoid it by ensuring loop variables update toward a clear exit condition.
* Q3. What does the variable i hold during the very first cycle of range(3, 50, 7)? 3 (the start value).

------------------------------
## BONUS — Number Guessing Game

secret = 42
for attempt in range(1, 6):
    guess = int(input(f"Attempt {attempt}/5 - Enter your guess: "))
    
    if guess == secret:
        print(f"Correct! You won in {attempt} attempts.")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")else:
    print(f"Game over! The number was {secret}")

## Bonus Questions:

*Q1. What operators are used to compare the guess to the secret? Comparison operators: == (equal to), < (less than), and > (greater than).
Q2. How do you track which attempt number the user is on? By setting the loop structure as range(1, 6), the loop counter variable automatically updates to hold values from 1 to 5.
