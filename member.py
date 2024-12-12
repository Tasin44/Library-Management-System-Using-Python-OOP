
# from person import Person
# class Member(Person):
#     def __init__(self, name, person_id):
#         super().__init__(name, person_id)
#         self.borrowed_books =[]

#     def borrow_book(self,library,book_title):
#         book = library.lend_book(book_title)#attempting to borrow book from the library by calling library’s lend_book() method.
        
#         if book:#Checks if the book is successfully borrowed (i.e., not None).
#             self.borrowed_books.append(book)
#             print(f"Member {self.name} borrowed '{book.name}'. ")

#     def return_book(self,library,book_title):#This method handles returning a borrowed book to the library.
#         for book_i in self.borrowed_books:#Iterates through the list of books the member has borrowed to find the book they want to return.
#             if book_i.name== book_title:
#                 self.borrowed_books.remove(book_i)
#                 library.return_book(book_i)
#                 print(f"Member {self.name} returned '{book_title}'")
#                 return
#         print(f"Member {self.name} doesn't have the book '{book_title}'.")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # Track borrowed books

    def borrow_book(self, library, book_title):
        if book_title in library.books:
            book = library.books[book_title]
            self.borrowed_books.append(book_title)  # Track the book as borrowed
            del library.books[book_title]  # Remove from library
            print(f"Member {self.name} borrowed '{book_title}'.")
        else:
            print(f"The book '{book_title}' is not available in the library.")

    def return_book(self, library, book_title):
        if book_title in self.borrowed_books:
            book = self.borrowed_books.pop(self.borrowed_books.index(book_title))
            library.books[book_title] = book  # Return the book to the library
            print(f"Member {self.name} returned '{book_title}'.")
        else:
            print(f"Member {self.name} doesn't have the book '{book_title}'.")
