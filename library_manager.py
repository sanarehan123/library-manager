import json
import os

LIBRARY_FILE = "library.json"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = input("Enter the publication year: ").strip()
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": int(year) if year.isdigit() else 0,
        "genre": genre,
        "read": read_status
    }
    
    library.append(book)
    print("Book added successfully!\n")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!\n")
            return
    print("Book not found.\n")

def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        search_term = input("Enter the title: ").strip().lower()
        results = [book for book in library if search_term in book["title"].lower()]
    elif choice == "2":
        search_term = input("Enter the author: ").strip().lower()
        results = [book for book in library if search_term in book["author"].lower()]
    else:
        print("Invalid choice!\n")
        return
    
    if results:
        print("Matching Books:")
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.")
    print()

def display_books(library):
    if not library:
        print("Your library is empty.\n")
        return
    print("Your Library:")
    for book in library:
        print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    print()

def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%\n")

def main():
    library = load_library()
    
    while True:
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
