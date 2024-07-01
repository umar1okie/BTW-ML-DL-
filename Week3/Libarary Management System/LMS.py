class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    # Getter for title
    def get_title(self):
        return self.__title

    # Setter for title
    def set_title(self, title):
        self.__title = title

    # Getter for author
    def get_author(self):
        return self.__author

    # Setter for author
    def set_author(self, author):
        self.__author = author

    # Getter for pages
    def get_pages(self):
        return self.__pages

    # Setter for pages
    def set_pages(self, pages):
        try:
            if pages <= 0:
                raise ValueError("Number of pages must be positive.")
            self.__pages = pages
        except ValueError as e:
            print(e)

    # Class method to calculate reading time based on reading speed (words per minute)
    @classmethod
    def calculate_reading_time(cls, pages, words_per_minute=250):
        # Assuming average words per page is 500
        words_per_page = 500
        total_words = pages * words_per_page
        reading_time = total_words / words_per_minute
        return reading_time

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Pages: {self.__pages}"


class Ebook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.__format = format

    # Getter for format
    def get_format(self):
        return self.__format

    # Setter for format
    def set_format(self, format):
        self.__format = format

    # Overriding __str__ method to include format
    def __str__(self):
        return f"Title: {self.get_title()}, Author: {self.get_author()}, Pages: {self.get_pages()}, Format: {self.__format}"


# Demonstrating the usage of Book and Ebook classes
try:
    # Creating an instance of Book
    my_book = Book("2008", "John Green", 305)
    print(my_book)  # Displaying initial book details

    # Using getters
    print("Title:", my_book.get_title())
    print("Author:", my_book.get_author())
    print("Pages:", my_book.get_pages())

    # Using setters
    my_book.set_title("James and the giant peach")
    my_book.set_author("Roald Dahl")
    my_book.set_pages(144)

    print(my_book)  # Displaying updated book details

    # Calculating reading time
    reading_time = Book.calculate_reading_time(my_book.get_pages())
    print(f"Estimated reading time: {reading_time:.2f} hours")

    # Creating an instance of Ebook
    my_ebook = Ebook("Brave New World", "Aldous Huxley", 288, "PDF")
    print(my_ebook)  # Displaying ebook details


except Exception as e:
    print(f"An error occurred: {e}")
