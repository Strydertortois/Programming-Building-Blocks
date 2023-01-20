

most_chapters = -1000
book_with_most = ''

with open('books_and_chapters.txt') as books_file:


    for line in books_file:
        parts = line.split(':')
        book = parts[0].strip()
        chapters = int(parts[1])
        scripture = parts[2].strip()
        
        print(f'Scripture: {scripture} Book: {book} Chapters: {chapters}')

        if chapters > most_chapters:
            most_chapters = chapters
            book_with_most = book

print(f"The book with the most chapters is: {book_with_most}")
print(f"It has {most_chapters} chapters.")

        

