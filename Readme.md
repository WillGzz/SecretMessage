# Message Decoder

This is a python script that scrapes data from a google docs URL
and shows a message based on the coordinates in the table

**Problem Description:**

You are provided with a Google Doc (similar to a given example) containing a list of Unicode characters and their corresponding positions within a 2D grid. Your objective is to develop a function that accepts the URL of such a Google Doc as input. This function should:

**Retrieve and Parse Data:** Fetch the document's content and extract the Unicode characters along with their x and y coordinates.
2.  **Construct the Grid:** Build a 2D grid representation of the characters, ensuring that any unspecified positions are filled with spaces.
3.  **Display the Message:** Print the grid to the console. When printed in a fixed-width font, the characters should form a graphic representing a sequence of uppercase letters, which constitutes the secret message.

**Input Format:**

* The Google Doc specifies the Unicode characters and their (x, y) coordinates.
* Coordinates are non-negative integers (minimum 0), and there is no upper bound on their values, allowing for arbitrarily large grids.

**Output Format:**

* The grid should be printed to the console, with each row on a new line.
* The characters in the grid, when displayed in a fixed-width font, should form a graphic of correctly oriented uppercase letters.
* The (0, 0) coordinate should correspond to the top-left corner of the grid.

**Constraints:**

* The input Google Doc will always adhere to the format of the provided example.
* Your code must be written in Python (preferred) or JavaScript.
* You may utilize external libraries.
* You may create helper functions, but the main function should:
    * Accept a single string argument representing the Google Doc URL.
    * Print the character grid to the console.

**Example:**

Given a simplified example document that draws the letter 'F':

█▀▀▀
█▀▀
█


The coordinates (0, 0) correspond to the top-left corner, and the x and y coordinates increase as shown in the example.

