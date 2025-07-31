class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False  

    def mark_as_read(self):
        self.is_read = True
        print(f"📘 '{self.title}' o‘qilgan deb belgilandi")

    def status(self):
        print(f"{self.title} — {'O‘qilgan' if self.is_read else 'O‘qilmagan'}")
