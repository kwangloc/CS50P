class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        self.current_page = 0
    
    def display(self):
        return self.content[self.current_page]

    def next_page(self):
        self.current_page += 1
        return self.content[self.current_page]

    def turn_page(self, page = 0):
        self.current_page = page-1
        return self.content[self.current_page]

class Library:
    def __init__(self):
        self.books = dict()
        self.id_counter = 0
        self.id_active = None

    def add_book(self, book):
        self.books[self.id_counter] = book
        self.id_counter += 1

    def find_book(self, title):
        for key, values in self.books.items():
            if values.title == title:
                # print(key)
                self.id_active = key
                return values
            
    def continue_reading(self):
        if self.id_active is not None:
            print(self.books[self.id_active].display())
        else:
            return "No book selected"

def main():
    book1 = Book("Book a", "John Doe", ["Chapter 1", "Chapter 2", "Chapter 3"])
    book2 = Book("Book b", "David Silvar", ["Chapter 1", "Chapter 2", "Chapter 3"])
    # book1.display()
    # book1.next_page()
    # book1.next_page()
    # book1.turn_page(1)

    library_1 = Library()
    library_1.add_book(book1)
    library_1.add_book(book2)

    found_book = library_1.find_book("Book a")
    print(found_book.display())
    print(found_book.next_page())
    print(found_book.next_page())

    found_book_2 = library_1.find_book("Book b")
    print(found_book_2.display())
    library_1.continue_reading()
    print(found_book_2.next_page())
    library_1.continue_reading()
    
if __name__ == "__main__":
    main()