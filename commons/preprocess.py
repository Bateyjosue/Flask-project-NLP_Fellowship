"""
This script helps preprocess text content
"""


class Preprocess:
    def __init__(self):
        """
        init
        """
        self.info = "Preprocess"

    def tokenize(self):
        """
        tokenize text
        """
        raise NotImplementedError

    def stemming(self):
        """
        text stemming
        """
        raise NotImplementedError
