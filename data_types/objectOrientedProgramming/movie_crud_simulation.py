class MovieCRUD:

    def __init__(self):
        self.movies = [
            {"id": 1, "title": "Inception", "year": 2010, "genre": "Sci-Fi",
             "rating": 8.8, "run_time": 148, "director": "Christopher Nolan"},
        ]

    
    def post(self, **kwargs):
        self.movies.append(kwargs)
        print("Movie record has been created...")


    def get(self):
        for movie in self.movies:
            print(movie)

    
    def retrieve(self, id=None):
        record = next((m for m in self.movies if m.get("id") == id), None)
        if record:
            print(record)
        else:
            print("No movie found with id:", id)

    
    def put(self, id=None, **kwargs):
        record = next((m for m in self.movies if m.get("id") == id), None)
        if record:
            record.update(kwargs)
            print("Movie record has been updated...")
        else:
            print("No movie found with id:", id)

    
    def delete(self, id=None):
        record = next((m for m in self.movies if m.get("id") == id), None)
        if record:
            self.movies.remove(record)
            print("Movie deleted...")
            self.get()
        else:
            print("No movie found with id:", id)



movie_instance = MovieCRUD()


movie_instance.post(id=2, title="Interstellar", year=2014, genre="Sci-Fi",
                    rating=8.6, run_time=169, director="Christopher Nolan")

movie_instance.get()

# Retrieve one
movie_instance.retrieve(id=2)

# Update
movie_instance.put(id=2, title="Interstellar (Updated)", rating=8.7)

# Delete
movie_instance.delete(id=2)
