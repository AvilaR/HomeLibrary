class Media:

    def __init__(self, name, date, genres):
        self.name = name
        self.date = date
        self.genres = []
        for g in genres:
            self.genres.append(g)

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_genres(self):
        return self.genres

    def set_name(self, new_name):
        self.name = new_name

