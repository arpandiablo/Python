class Library:
    def __init__(self):
        self.bname = []
        self.count = 0
    def add_book(self,book_name):
        self.bname.append(book_name)
        self.count = len(self.bname)
    def display(self):
        print(f"The number of books in library is {self.count} and they are : ")
        print(self.bname)

l1 = Library()
l1.add_book("The Hobbit 1")
l1.add_book("The Hobbit 2")
l1.add_book("The Hobbit 3")
l1.display()