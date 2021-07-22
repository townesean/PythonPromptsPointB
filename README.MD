1. Work Assignments
===================
Tasks for ACME Inc employees are assigned by putting their ID numbers into a list, one time for each day they'll work that task. As shifts are planned well in advance, the lists for each task will contain up to 99 integers. When an employee is scheduled for the same task too many times, they'll complain about it until they're taken off the task completely. Some tasks are worse than others, so the number of scheduled assignments before an employee will refuse to do a task varies depending on the task. You figure you can speed things up by automating the removal of the employees who have been assigned a task too many times before they even get a chance to start complaining.

Write a function called solution(data, n) that takes in a list of less than 100 integers and a number n, and returns that same list but with all of the numbers that occur more than n times removed entirely. The returned list should retain the same ordering as the original list - you don't want to mix up those carefully-planned shift rotations! For instance, if data was [5, 10, 15, 10, 7] and n was 1, solution(data, n) would return the list [5, 15, 7] because 10 occurs twice, and thus was removed from the list entirely.

Test Case 1:
Inputs:
(int list) data = [1, 2, 3]
(int) n = 0
Output:
(int list) []

Test Case 2:
Inputs:
(int list) data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
(int) n = 1
Output:
(int list) [1, 4]

Test Case 3
Inputs:
(int list) data = [1, 2, 3]
(int) n = 6
Output:
(int list) [1, 2, 3]


2. Passing Coded Messages
=========================
ACME Inc employees like to pass coded messages. To avoid detection, you need to combine sets of digits 0-9 to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of digits to work with.

You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

Test Case 1:
Input:  solution([3, 1, 4, 1]) 
Output: 4311

Test Case 2:
Input:  solution([3, 1, 4, 1, 5, 9]) 
Output: 94311


3. Avoid Getting Voluntold!
===========================
ACME Inc CEO has installed new flooring outside analysts' cubicles. It looks like a chessboard, and every morning analysts are told to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight! Worse, if you take too much time solving the puzzle, you get "voluntold" onto undesirable projects.

To help yourself get to your cubicle every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle. The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape). Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Test Case 1:
Inputs:
(int) src = 19
(int) dest = 36
Output:
(int) 1

Test Case 2:
Inputs:
(int) src = 0
(int) dest = 1
Output:
(int) 3
