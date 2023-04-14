"""
Program Name: bookrecsgui.py
Created by: Isaac Hill
Last Modified Date: 03/15/21

Description: This program when ran will pop up a window with three buttons, Friends, Recommend, and Report. When the user presses the
friends button a window will pop up asking the user for a reader. The program will check if it is a valid reader and will open another
window with the reader's friends. When the user presses the Recommend button a window will pop up asking the user for a reader. The 
program will check if that is a valid reader and will open another window with the read's recommended books. When the user presses the 
Report button a window will pop up showing every reader's friends and recommended books.

class BookRecsGUI(): Displays buttons that when pressed interact with bookrecs.py
    def getFriends(): asks user for reader and will create message box with reader's friends.
    def getRecommended(): asks user for reader and will create message box with reader's recommended books.
    def getReport(): creates message box that shows each reader's friends and recommended books.

I declare that the following source code was written solely by me. I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project if I am found in violation of this policy. 
I also understand future CS classes and jobs will be more difficult as a result of not doing my own work.
"""

from breezypythongui import EasyFrame
import bookrecs

class BookRecsGUI(EasyFrame):
    """
    BookRecsGUI class: Displays buttons that when pressed interact with bookrecs.py

    Class attributes:
        addButton (Friends): Adds button when pressed runs getFriends()
        addButton (Recommend): Adds button when pressed runs getRecommended()
        addButton (Report): Adds button when pressed runs getReport()
    """
    def __init__(self):
        EasyFrame.__init__(self, title = "Book Recommendations", background = "#B5FFBF", width = 300, height = 50)

        self.addButton(text = "Friends", row = 0, column = 1, command = self.getFriends)
        self.addButton(text = "Recommend", row = 0, column = 2, command = self.getRecommended)
        self.addButton(text = "Report", row = 0, column = 3, command = self.getReport)
    
    def getFriends(self):
        """
        This function will open a prompterbox that will ask the user for the reader name. If the reader name is invalid
        it will open an error message box telling the user that there is no such user. If the reader name is valid
        it will open a message box and have a message with the reader's friend using bookrecs' friends function.

        Parameters:
            None

        Returns:
            None
        """
        try:
            #Creates a prompter box asking user for reader name
            name = self.prompterBox(title = "Friends", promptString = "Enter Reader Name:")
            #Opens a message box with content from bookrecs' friends function shown.
            self.messageBox(title = f"Friends of {name}", message = "\n".join(bookrecs.friends(name)))
        except KeyError:
            #Opens a message box with an error message
            self.messageBox(title = "Error", message = "No such reader.")
    
    def getRecommended(self):
        """
        This function will open a prompterbox that will ask the user for the readers name. If the reader name is invalid
        it will open an error message box telling the user that there is no such user. If the reader name is valid it will
        open a message box showing all of the reader's recommended books using bookrecs' reccomend function.

        Parameters:
            None

        Returns:
            None
        """
        #Runs code to see if a KeyError pops up, if so create an error message box
        try:
            #Creates a prompter box asking user for reader name
            name = self.prompterBox(title = "Recommendations", promptString = "Enter Reader Name:")
            recommendedBooks = []
            #For each book in the list of tuples returned by recommend, create a list with the tuples combined
            for book in bookrecs.recommend(name):
                recommendedBooks.append(f"{book[0]} {book[1]}, {book[2]}")
            #Opens a message box with content from recommendedBooks list shown
            self.messageBox(title = f"Recommendations for {name}", width = 100, height = 25, message = "\n".join(recommendedBooks))
        except KeyError:
            #Opens a message box with an error message
            self.messageBox(title = "Error", message = "No such reader.")

    def getReport(self):
        """
        This function will sort the list of keys from bookrecs' reader_rating dictionary to get all the readers. It will then
        make a big list with each item being a line to be shown using bookrec's friends and recommend function. 
        Then opens a message box with the content being shown to the user.

        Parameters:
            None

        Returns:
            None
        """
        report = []
        #Sorts list of keys from bookrecs' reader_ratings
        readers = sorted(bookrecs.reader_ratings.keys())
        #For each reader show friends and show each book recommended for reader.
        for name in readers:
            report.append(f"Recommendations for {name} from {bookrecs.friends(name)[0]} and {bookrecs.friends(name)[1]}:")
            for book in bookrecs.recommend(name):
                report.append(f"\t{book[0]} {book[1]}, {book[2]}")
            #Adds empty string to list so that a empty line is added
            report.append("")
        #Oepns a message box with content from report shown
        self.messageBox(title = "Report", width = 100, height = 50, message = "\n".join(report))
    
def main():
    #Creates instance of class and runs main loop
    bookrecsgui = BookRecsGUI()
    bookrecsgui.mainloop()
    
if __name__ == "__main__":
    main()
