#Library Management System
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been marked as borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")


    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been marked as returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"Apologies, the book '{book.title}' is currently unavailable")
        else:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"The book '{book.title}' was not borrowed.")


    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")


#An interactive code allowing members to borrow books
def main():
    book1 = Book("The Hobbit", "J.R.R. Tolkien")
    book2 = Book("Anna Karenina", "Leo Tolstoy")
    book3 = Book("The Hunger Games", "Suzanne Collins")

    member = LibraryMember("Maria", "M001")

    while True:
        print("\nLibrary Management System")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable books to borrow:")
            available_books = [book for book in [book1, book2, book3] if not book.is_borrowed]
            for i, book in enumerate(available_books, start=1):
                print(f"{i}. {book.title} by {book.author}")

            if available_books:
                book_choice = int(input("Enter the number of the book you want to borrow: ")) -1
                member.borrow_book(available_books[book_choice])
            else:
                print(f"There are no books available to borrow")

        elif choice == "2":
            if member.borrowed_books:
                print("\nBooks currently borrowed by you:")
                for i, book in enumerate(member.borrowed_books, start=1):
                    print(f"{i}. {book.title} by {book.author}")

                book_choice = int(input("Enter the number of the book you want to return: ")) - 1
                member.return_book(member.borrowed_books[book_choice])
            else:
                print(f"There are no books currently borrowed")

        elif choice == "3":
            member.list_borrowed_books()

        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



















