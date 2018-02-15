import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ This constructor allows a Movie object to be instantiated """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ This function allows the webbrowser to open the trailer of the selected movie """
        webbrowser.open(self.trailer_youtube_url)
