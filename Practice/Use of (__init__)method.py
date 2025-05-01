# Use of (__init__)method to initialize the class
class Book:
    # Add the __init__ method here
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    
# Create a book object
# Your code here
my_book=Book('Harry Potter', 'J.K. Rowling', 400)

# Print book details
print(f"'{my_book.title}' by {my_book.author}, {my_book.pages} pages")