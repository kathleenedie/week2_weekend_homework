import unittest

from src.songs import Songs

class TestSongs(unittest.TestCase):

    def setUp(self):
        self.song_1 = Songs("The Chain", "Fleetwood Mac")
        self.song_2 = Songs("Club Tropicana", "Wham!")
    
    def test_song_has_name(self):
        self.assertEqual("The Chain", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("Fleetwood Mac", self.song_1.artist)
    
    