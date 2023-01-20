


with open('books.txt') as books_handle:
    for book in books_handle:
        print(book.strip())