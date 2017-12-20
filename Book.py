from Media import Media as med


class Book(med):

    def __init__(self, name, date, genres, author, pages):
        super().__init__(name, date, genres)
        self.author = author
        self.pages = pages

    def get_author(self):
        return self.author

    def get_pages(self):
        return self.author

    def set_author(self, new_author):
        self.author = new_author

    def set_pages(self, new_pages):
        self.pages = new_pages
