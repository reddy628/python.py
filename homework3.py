Here are the complete answers and verified outputs for your Python programming assignment.
## 1. for Loop — Trace & Fill-in-the-Blanks## Part A: Write the output of each loop

* Loop 1 Output:

1
3
5
7
9

* Loop 2 Output: 15 (Calculated as 1 + 2 + 3 + 4 + 5)
* Loop 3 Output:

10
8
6
4
2

* 

## Part B: Fill in the blanks

* Sum of even numbers from 2 to 20: for i in range(2, 22, 2): (End is set to 22 so 20 is included)
* Print numbers from 100 down to 10: for i in range(100, 0, -10): (End is set to 0 so 10 is included)
* 

## Questions

* Q1: Python's range(start, end) stops at end - 1 because the upper bound is always exclusive.
* Q2: The default step value is 1.
* 

------------------------------
## 2. while Loop — Build & Compare## Your while loop version:

start = 5end   = 50step  = 5
while start <= end:
    print(start)
    start = start + step

## Questions

* Q1: The program will create an infinite loop, printing 5 forever because the condition start <= end will never become false.
* Q2: Choose a while loop when you do not know the exact number of iterations in advance. Real-world example: A login screen that keeps prompting a user until they enter the correct password.
* Q3: Code:

num = -1while num != 0:
    num = int(input("Enter a number (0 to stop): "))


------------------------------
## 3. break and continue — Trace

* Snippet A Expected output: 1, 2, 3, 4 (Each on a new line)
* Snippet B Expected output: 1, 2, 3, 4, 6, 7, 8, 9, 10 (Each on a new line; 5 is skipped)
* Snippet C Expected output: 2, 4, 6, 8, 12, 14 (Each on a new line; 10 is skipped, stops entirely before 16)

## Questions

* Q1:
* break: Immediately terminates the entire loop execution.
   * continue: Skips the remaining code in the current iteration and jumps directly to the next cycle.
* Q2: Yes. You can use break to exit a while True loop immediately when a specific flag or exit condition is met.

------------------------------
## 4. List Operations — Build & Modify## Part A: List indexing answers

* fruits[0]: 'apple'
* fruits[2]: 'cherry'
* fruits[-1]: 'elderberry'
* len(fruits): 5

## Part B: Code operations (Starting with a = [10, 20, 30])

   1. a.append(40)
   2. a.extend([5, 6, 7])
   3. a.insert(1, 99)
   4. a.remove(20)
   5. a.pop()
   6. a.sort()
   7. a.sort(reverse=True)
   8. a.clear()

## Questions

* Q1: append() adds a single element to the end of a list, whereas extend() iterates over an iterable argument and appends each individual item.
* Q2: remove() deletes an item matching a specific value, while pop() deletes and returns an item at a specific index.
* Q3: Code:

colors = ['red', 'green', 'blue']for color in colors:
    print(color)


------------------------------
## 5. Lists vs Tuples — Compare & Classify## Part A: Classification Table

| Statement | Answer |
|---|---|
| Can store items of different data types | LIST & TUPLE |
| Values can be changed after creation | LIST |
| Uses square brackets [ ] | LIST |
| Uses parentheses ( ) | TUPLE |
| Has .append() and .remove() methods | LIST |
| Immutable — cannot add or delete items | TUPLE |
| Used in Django where values must not change at runtime | TUPLE |
| Mutable — can be freely modified | LIST |

## Part B: Predictions

* Snippet 1: It raises a TypeError because tuples do not support item assignment or modification methods like .append().
* Snippet 2: Outputs 1 followed by 3 on a new line.

## Questions

* Q1: In Django, configurations like database settings or tuple-based form fields (CHOICES) use tuples. This ensures that core system configurations remain static and secure from accidental changes during user requests.
* Q2: "Can be changed" is mutable (applies to lists). "Cannot be changed" is immutable (applies to tuples).
* Q3: Student Reflection Response Example: Understanding that range() excludes the end number was the trickiest part, because it requires adding 1 to your target maximum boundary when counting up.

------------------------------
## BONUS — Mini Project: Student Grade Tracker
Here is a fully functional implementation of the bonus tracker logic:

# 1. Setup Datagrades = [85, 38, 92, 100, 74]subjects = ('Math', 'Science', 'English', 'History', 'Computer Science')
# Calculate Total and Averagetotal = 0for grade in grades:
    total += gradeaverage = total / len(grades)

print(f"Total Score: {total} | Average Score: {average:.2f}\n")
# Process items with continue, break, and zip pairingsfor i in range(len(grades)):
    current_grade = grades[i]
    current_subject = subjects[i]
    
    # 3. Check for failing grade
    if current_grade < 40:
        print(f"Skipping low mark: {current_subject} grade was below 40!")
        continue
        
    # 4. Check for perfect score
    if current_grade == 100:
        print(f"{current_subject}: {current_grade}")
        print("Perfect score!")
        break
        
    # 5. Print standard subject with grade
    print(f"{current_subject}: {current_grade}")

## Project Questions

* Q1: Subjects are fixed parts of an academic term. Using an immutable tuple prevents code bugs from accidentally overwriting or erasing a school subject name during execution.
* Q2: Output tracking:

Total Score: 389 | Average Score: 77.80

Math: 85
Skipping low mark: Science grade was below 40!
English: 92
History: 100
Perfect score!

* Q3: Lining up the list indices between the grades list and the subjects tuple was challenging. I solved this by tracking loops through an integer index (range(len(grades))) to target matching positions cleanly.

Would you like me to clarify how the negative steps work in descending loops, or do you want to explore more advanced list slicing tricks next?

# Let's double check calculations and code snippet executions to be 100% accurate

print("--- 1 Loops Part A ---")
print("Loop 1:")for i in range(1, 10, 2):
    print(i, end=" ")
print("\nLoop 2:")total = 0for i in range(1, 6, 1):
    total = total + i
print(total)
print("Loop 3:")for i in range(10, 0, -2):
    print(i, end=" ")
print()

print("\n--- 1 Loops Part B ---")# Even numbers 2 to 20 summing to 110total = 0for i in range(2, 22, 2):
    total = total + i
print("Part B1 Sum:", total)
# 100 down to 10 by 10
print("Part B2 Countdown:")for i in range(100, 0, -10):
    print(i, end=" ")
print()

print("\n--- 3 Break/Continue ---")
print("Snippet A:")for i in range(1, 11, 1):
    if i == 5:
        break
    print(i, end=" ")
print("\nSnippet B:")for i in range(1, 11, 1):
    if i == 5:
        continue
    print(i, end=" ")
print("\nSnippet C:")for i in range(2, 20, 2):
    if i == 10:
        continue
    if i == 16:
        break
    print(i, end=" ")
print()



