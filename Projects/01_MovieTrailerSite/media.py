import webbrowser


# Creates the class Movie in order to store information about my
# favorite movies
class Movie():
    # The information being stored is
    # Movie title
    # Movie poster
    # Movie trailer
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Enables the trailer to be shown in a web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
