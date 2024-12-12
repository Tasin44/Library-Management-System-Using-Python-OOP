class Library():
    def __init__(self):
        self.books =[]
        self.lent_books =[]

    def add_book(self,book):#class Librarian has access
        self.books.append(book)#here,must be added the entire Book object(name,author) rather than title 

    def remove_book(self,book_title):#class Librarian has access
        for book_i in self.books:
            if book_i.name==book_title:
                self.books.remove(book_i)#will remove the book based on title
                return 
        print(f"Book '{book_title}' not found in library.")    


    def lend_book(self,book_title):#class Member has access
        for book_i in self.books:
            if book_i.name == book_title:
                #self.books.remove(book_i)#after borrowing a book,it'll be removed from library
                self.lent_books.append(book_i)#after borrowing a book,it'll be added to lent_books list
                return book_i
        print(f"Book '{book_title}' is unavailable")
        return None
    
    def return_book(self,book):#class Member has access
        if book in self.lent_books:
            self.lent_books.remove(book)
            # ei book ta dhar nichilam,ekhn ferot dicchi.
            # so it'll be removed from lent_books list & append to the library(ferot deyar por library te rekho dilam)
            self.books.append(book)
        else:
            print(f"Error: '{book.name}' was not borrowed from the library.")
        
    def display_books(self):
        if self.books:
            print("Available books in the library:")
            for book in self.books:
                print(f" -{book.name} by {book.author}")
        else:
            print("No books are available in the library.")
print("Library module executed successfully.")