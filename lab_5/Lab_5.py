class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f'назваение книги: {self.title}, Автор: {self.author}, Год издания: {self.year}'
book = Book('Мертвые души', 'Николай Гоголь', '1842')
print(print(book.get_info()))