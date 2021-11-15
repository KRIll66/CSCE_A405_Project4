# CSCE_A405_Project4
Sudoku AI
CSCE A405 Programming Assignment 4
Due Tuesday, November 23, 2021, at 11:59 PM

Purpose:  The goal of this assignment is to gain an understanding of constraint satisfaction problems and how to solve them.

Sudoku is a popular puzzle in which the user must complete a 9x9 grid with the digits 1 through 9, such that every row, column, and 3x3 box contains exactly one copy of each digit. (An example puzzle, together with its solution, is shown on R&N p. 213.) Your task is to design, test, debug, and verify the correct operation of a program that uses constraint propagation to fill in a given Sudoku grid with digit values representing a correct solution.

To solve this problem, your program should read an initial Sudoku board from an interactively specified file, setting each defined position of the puzzle to the specified value, and initialize the remaining (initially blank) positions of the puzzle to the “domain” {1, 2, 3, 4, 5, 6, 7, 8, 9}, i.e., every possible value that could be in that position. Your program should then go about eliminating possible values until every puzzle entry contains exactly one value. Note that the textbook (p. 214) suggests both straightforward and clever ways of doing this, including “naked triples”. (HINT: In general, if k entries in a given row, column, or box contain permutations of k distinct digits only, then those digits may be eliminated from the remaining 9-k entries in that row, column, or box; for example, if four entries in a given row contain {1, 4}, {4, 5}, {1, 5, 9} and {4, 9}, then digits 1, 4, 5, and 9 may be eliminated from the remaining five entries in that row.)

Sudoku puzzles are typically rated from one (easy) to five stars (very difficult).  Once you’ve gotten a basic Sudoku solver to work, try it on increasingly more difficult problems, adding more functionality (“cleverness”) to your program as you go. (Thousands of examples can be found in newspapers, puzzle magazines, and books, and on the internet.)  

Your final report should describe your solution, paying particular attention to the techniques you used to eliminate values in each position’s “domain”. Include a table showing your test problems and their difficulty levels, as well as how well your program performed on these puzzles. (A fair amount of data gathering is a good idea here!)  Conclude your report by ranking your program’s competence level (from one to five stars) in solving Sudoku problems. Part of your grade for this assignment will reflect the difficulty level of problems your code can correctly handle.

Submit your source code and final report via email attachments. Clearly indicate the name and preferred email address of each member of your team at the top of your source code and report. I will run your program, assess its problem-solving capability, read your final report, and return your grade via email.
