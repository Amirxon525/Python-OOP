class Book:
    def __init__(self, title, author, is_read=False):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True
        print("Kitob o‘qilgan deb belgilandi")

    def status(self):
        print("O‘qilgan" if self.is_read else "O‘qilmagan")
