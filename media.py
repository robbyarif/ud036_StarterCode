"""This is media module.

This module contain class definition and constructor for creating
movie instances.
"""

import webbrowser


class Movie:
    """Movie class defines title, storyline, image and youtube trailer url.

    Attributes:
            title (str)				 : title of the movie
            storyline (str)			 : short synopsis of the movie
            poster_image_url (str)	 : poster image
            trailer_youtube_url (str): youtube trailer link
    """

    def __init__(
            self, movie_title, movie_storyline,
            poster_image, trailer_youtube):
        """Return an instance of Movie class"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
