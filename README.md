# queens-Hansen-page

# Algorithm Name
Binary Search Visualizer

#Demo screenshot

Please see demo screen 1,2 

##Problem break

I chose "binary search" as the algorithm for this project because it is an efficient and well-structured search algorithm that effectively embodies the concept of computational thinking. Moreover, it is the algorithm I use most frequently in my daily work, and I really like it. I have chosen it as an attempt for this assignment. This can enhance my application of it.

#Decomposition

Parse the user’s input string into a list of integers.

Sort the list before applying binary search.

Implement the binary search algorithm using "low", "mid", and "high".

Record each step of the algorithm in a readable text format.

Build a Gradio UI to connect user input with the algorithm output.

#Pattern Recognition

Binary search follows a repeated pattern: Calculate the middle index.

Compare the middle value with the target.

Discard half of the search range.

Each iteration repeats the same logic until the target is found or the range is empty.

#Abstraction

The user only sees:The original list, sorted list, target value and a step-by-step explanation of the search

If the list contains non-integer values, or is empty, the user only sees a short message like “Please enter only integers separated by commas.”

The user does not need to see the internal Python variables or exceptions.

#Algorithm Design

Convert user input into integers.

Sort the list.

Use a loop to repeatedly narrow the search range.

Stop when the target is found.

Display whether the target is found and all intermediate steps.

#Hugging face link

https://huggingface.co/spaces/hasne21/binary-search-visualizer

#Author & Acknowledgment

Hansen Du

CISC 121 materials and assignment instructions

Gradio documentation

Chatgpt5 used at Level 4



