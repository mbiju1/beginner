class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} by {self.author} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} by {self.author} has been checked in.")
        else:
            print(f"{self.title} is already checked in.")

    def __str__(self):
        status = "Checked out" if self.checked_out else "Available"
        return f"{self.title} by {self.author} ({self.publication_date}), Genre: {self.genre}, Status: {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def search_by_genre(self, genre):
        return [book for book in self.books if book.genre == genre]

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_status(self, checked_out):
        return [book for book in self.books if book.checked_out == checked_out]

    def list_books(self):
        for book in self.books:
            print(book)

def main():
    library = Library()

    book1 = Book("The Catcher in the Rye", "J.D. Salinger", "Fiction", "1951")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", "1960")
    book3 = Book("1984", "George Orwell", "Dystopian", "1949")
    book4 = Book("Pride and Prejudice", "Jane Austen", "Fiction", "1813")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    while True:
        print("\nLibrary Management System")
        print("1. List Books")
        print("2. Search by Author")
        print("3. Search by Genre")
        print("4. Search by Title")
        print("5. Search by Status")
        print("6. Check Out Book")
        print("7. Check In Book")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.list_books()
        elif choice == "2":
            author = input("Enter author name: ")
            results = library.search_by_author(author)
            for book in results:
                print(book)
        elif choice == "3":
            genre = input("Enter genre: ")
            results = library.search_by_genre(genre)
            for book in results:
                print(book)
        elif choice == "4":
            title = input("Enter title: ")
            results = library.search_by_title(title)
            for book in results:
                print(book)
        elif choice == "5":
            status = input("Enter status (Available or Checked out): ").lower()
            checked_out = status == "checked out"
            results = library.search_by_status(checked_out)
            for book in results:
                print(book)
        elif choice == "6":
            title = input("Enter the title of the book to check out: ")
            book = next((b for b in library.books if b.title.lower() == title.lower()), None)
            if book:
                book.check_out()
            else:
                print(f"Book with title '{title}' not found in the library.")
        elif choice == "7":
            title = input("Enter the title of the book to check in: ")
            book = next((b for b in library.books if b.title.lower() == title.lower()), None)
            if book:
                book.check_in()
            else:
                print(f"Book with title '{title}' not found in the library.")
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
