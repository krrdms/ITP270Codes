import requests


class movieObj:

    def __init__(self, movie):
        self.__title = movie['Title']
        self.__year = movie['Year']
        self.__rated = movie['Rated']
        self.__runTime = movie['Runtime']
        self.__genre = movie['Genre'].split(", ")
        self.__director = movie['Director'].split(", ")
        self.__writer = movie['Writer'].split(", ")
        self.__actors = movie['Actors'].split(", ")
        self.__plot = movie['Plot']
        self.__language = movie['Language']
        self.__type = movie['Type']
        if "totalSeasons" in movie.keys():
            self.__seasons = movie['totalSeasons']
        self.__response = bool(movie['Response'])

    @property
    def title(self): return self.__title

    @property
    def year(self): return self.__year

    @property
    def rated(self): return self.__rated

    @property
    def runTime(self): return self.__runTime

    @property
    def genre(self): return self.__genre

    @property
    def director(self): return self.__director

    @property
    def writer(self): return self.__writer

    @property
    def actors(self): return self.__actors

    @property
    def plot(self): return self.__plot

    @property
    def language(self): return self.__language

    @property
    def type(self): return self.__type

    @property
    def seasons(self): return self.__seasons

    @property
    def response(self): return self.__response


def magic(title):
    with open("keys/movie.key") as keyFile:
        key = keyFile.read()
    searchURL = "http://www.omdbapi.com/?t=" + title + "&apikey=" + key
    movieRequest = requests.get(searchURL)
    return movieRequest.json()


def printMovie(movie):
    if movie.response:
        print("[+]Movie: " + movie.title + " Loaded")
        print()

    print("[ ]Title:", movie.title)
    print("[ ]Genre:", movie.genre)
    print("[ ]Rated:", movie.rated)
    print("[ ]Year:", movie.year)
    print("[ ]Writer:", movie.writer)
    print("[ ]Actors:", movie.actors)
    print("[ ]Plot:", movie.plot)


def main():
    # main script
    while True:
        title = input("[?]Enter Movie Title: ")
        if len(title) == 0:
            return
        movieData = magic(title)
        movie = movieObj(movieData)
        printMovie(movie)


if __name__ == "__main__":
    # execute only if run as a script
    main()
