class Movie():
    """ This is movie Class to keep the data attributes for different movie instances  """

    def __init__(self, title, storyline, poster_image_url='', trailer_youtube_url=''):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
