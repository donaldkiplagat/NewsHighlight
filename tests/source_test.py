import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Source Class
    """
    def setup(self):
        """
        Set up method that will run before every Test
        """
        self.new_source = Source(5432,"Donald Kiplagat","Test to see if Source is retrieved","TestUrl","TestUrlToImage","TestTime","The article itself")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sourcce,Source))
