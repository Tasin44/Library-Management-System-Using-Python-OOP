
from person import Person
        
class Librarian(Person):
    def __init__(self,name,person_id):
        super().__init__(name,person_id)
        self.books =[]#Initializes an empty list to store the books that the member has borrowed. 
        
    def add_book(self,library,book):#library class method add_book,so named library putted
        library.add_book(book)#here,must be added the entire Book object(name,author) rather than title 
        print(f"Book '{book.name}' added to the library")
    
    def remove_book(self,library,book_title):#library class method add_book,so named library putted
        library.remove_book(book_title)
        print(f"Book '{book_title}' removed from the library. ")