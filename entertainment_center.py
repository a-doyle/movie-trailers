import fresh_tomatoes
import media

# Saving Private Ryan movie: title, storyline, poster, trailer
saving_private_ryan = media.Movie("Saving Private Ryan",
                                "The mission is a man",
                                "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=RYID71hYHzg")

# The Avengers movie: title, storyline, poster, trailer
avengers = media.Movie("The Avengers",
                       "Earth's mightiest heroes",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# Spirited Away movie: title, storyline, poster, trailer
spirited_away = media.Movie("Spirited Away",
                            "A young girl battles to save her parents",
                            "http://img.moviepostershop.com/spirited-away-movie-poster-2002-1020407964.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

# School of Rock movie: title, storyline, poster, trailer
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

# Kingsman: The Secret Service movie: title, storyline, poster, trailer
kingsman = media.Movie("Kingsman: The Secret Service",
                       "Street boy turned spy",
                       "https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=m4NCribDx4U")

# You're Next movie: title, storyline, poster, trailer
youre_next = media.Movie("You're Next",
                         "Stalked by masked killers in the family home",
                         "https://upload.wikimedia.org/wikipedia/en/c/c2/YoureNext2011Film.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=ufUQWpEkbf0")

# Sets the list of movies that will be passed to the media file
movies = [saving_private_ryan,
          avengers,
          spirited_away,
          school_of_rock,
          kingsman,
          youre_next]

# Opens the HTML in a webbrowser via the freshy_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
