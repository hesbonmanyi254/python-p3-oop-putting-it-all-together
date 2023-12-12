class Book:
    def __init__(self, title, author, pages):
        """
        Constructor for the Book class.

        Parameters:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - pages (int): The total number of pages in the book.
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1  # The book is initially open at page 1

    def turn_page(self, page_count):
        """
        Simulates turning the pages of the book.

        Parameters:
        - page_count (int): The number of pages to turn.

        This method updates the current_page attribute.
        """
        self.current_page += page_count

    def open_book(self):
        """
        Returns a string representation of the book's current state.

        Returns:
        str: A string containing the book's title, author, and the current page.
        """
        return f"{self.title} by {self.author}, Page {self.current_page}"
