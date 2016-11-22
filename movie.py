import webbrowser

class Movie():

    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_youtube_trailer):
        """Constructor method taking the parameters and assigning them to instance variables."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_youtube_trailer

    def show_trailer(self):
        """Opens a webbrowser and requests a YouTube video by passing the trailer_youtube_url."""
        webbrowser.open(self.trailer_youtube_url)

