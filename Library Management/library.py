# Simple Library Management System

library = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Book
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = {
            "title": title,
            "author": author
        }

        library.append(book)
        print("Book added successfully!")

    # View Books
    elif choice == "2":
        if len(library) == 0:
            print("No books available.")
        else:
            print("\nBooks in Library:")
            for index, book in enumerate(library, start=1):
                print(f"{index}. {book['title']} by {book['author']}")

    # Search Book
    elif choice == "3":
        search = input("Enter book title to search: ")

        found = False

        for book in library:
            if book["title"].lower() == search.lower():
                print(f"Found: {book['title']} by {book['author']}")
                found = True

        if not found:
            print("Book not found.")

    # Delete Book
    elif choice == "4":
        delete_title = input("Enter book title to delete: ")

        found = False

        for book in library:
            if book["title"].lower() == delete_title.lower():
                library.remove(book)
                print("Book deleted successfully!")
                found = True
                break

        if not found:
            print("Book not found.")

    # Exit
    elif choice == "5":
        print("Exiting Library System...")
        break

    else:
        print("Invalid choice! Please try again.")