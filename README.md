# Design Pattern - Memento
The aim of the project was to implement the design pattern to the selected issue. 
Memento is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.

## Use Case
We used the Memento Design Pattern to simulate a text editor 'undo' function. 
Before performing any operation, the app records the state of all objects and saves it in some storage. 
Later, when a user decides to revert an action, the app fetches the latest snapshot from the history and uses it to restore the state of all objects.

**Tools:**
* Python 3 - application code
* Doxygen - a documentation generator

## How to run
To run the program, enter the `make` command in the terminal.
