class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

    def activate(self):
        self.is_active = True
        print("Foydalanuvchi faollashtirildi.")

    def deactivate(self):
        self.is_active = False
        print("Foydalanuvchi bloklandi.")
