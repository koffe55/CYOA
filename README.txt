********CYOA********
Description: 		A 'Choose Your Own Adventure' novella reader and GUI
Created:		19 April 2013
Author:			Jeffrey Dowell
Organization:		University of Maryland, College Park
Contact:		jdowell55@gmail.com
********************

****Introduction****
CYOA is a project designed to enable writers and creators of 'Choose Your Own Adventure' styled novellas that center around interactive, decision-based reading. Traditionally, these books have been a physical medium that required the reader to turn to a specific page to commit a decision in the story and be faced with content that was written for the implications of that decision. This project aims to create a simple, easy format for writers to create a digital version of such a novella that is presented using a simple GUI to make decisions and record your path through the story. 

The CYOA platform is written in Python, and is essentially composed of two modules: StoryReader.py, which implements methods to manage the text of the story and enumerate chioces, and cyoagui.py, which implements a GUI using Tkinter. 

****Install****
To run the platform natively, you need to have Python 2.7 installed on your computer. An executable version of the GUI is published, which obviously does not require Python to run. An 'about.txt' file must reside in the directory where cyoagui.py is launched, as well as a file named 'story.txt' which contains your story.

****Format of Story****
The story is written using square brackets to denote text presented to the reader and parenthesis to denote choices. A piece of the story can be followed by any number of choices. 

Example syntax :

[12]
It's been a long time since you've been able to lay down and rest. Your supplies are running low, and you estimate that your rations will last another three days at best. Nevertheless, there are still miles to go before the next station. What do you do?
(84) Go back the the last station. They will have food for you to restock.
(124) Persist on, and hope that you can make it through the desert.
(3) Open one of your three battery cartridges and hope you have enough juice to make a high-powered phone call back to HQ.

This example demonstrates a prompt ('It's been a long time.....for you to restock.') numbered 12. The three options of 84 124, and 3, whose numbers are not visible to the reader, inform the program of which prompt should be delivered if the reader makes its associated decision. 


