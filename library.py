books = []

while True:
    print("\n1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        title = input("Enter book name:")
        subject = input("Enter subject:")
        books.append([title, subject, "Available"])
        print("Book added!")

    elif choice == "2":
        print("\nAll Books:")
        for i, book in enumerate(books,1):
            print(f"{i}. {book[0]} - {book[1]} - {book[2]}")

    elif choice == "3":
        print("\nAvailable Books:")
        available_books = []
        for i, book in enumerate(books):
            if book[2] == "Available":
                available_books.append(book)
                print(f"{len(available_books)}. {book[0]} - {book[1]}")

        if available_books:
            book_name = input("Enter book name to borrow:")
            for book in books:
                if book[0] == book_name and book[2] == "Available":
                    book[2] = "Borrowed"
                    print("Book borrowed!")
                    break
            else:
                print("Book not found or not available!")

    elif choice == "4":
        print("\nBorrowed Books:")
        borrowed_books = []
        for i, book in enumerate(books):
            if book[2] == "Borrowed":
                borrowed_books.append(book)
                print(f"{len(borrowed_books)}. {book[0]} - {book[1]}")

        if borrowed_books:
            book_name = input("Enter book name to return:")
            for book in books:
                if book[0] == book_name and book[2] == "Borrowed":
                    book[2] = "Available"
                    print("Book returned!")
                    break
            else:
                print("Book not found or not borrowed!")

    elif choice == "5":
        break

    else:
        print("Invalid choice!")